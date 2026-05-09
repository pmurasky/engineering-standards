import { tool } from "@opencode-ai/plugin";
import { spawn } from "child_process";
import { fileURLToPath } from "url";
import { dirname, join } from "path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

/**
 * Run a Python script from the scripts/ directory.
 * @param {string} scriptName - Name of the Python script (e.g., "install_standards.py")
 * @param {string[]} args - Arguments to pass to the script
 * @param {string} cwd - Working directory for the script
 * @returns {Promise<{stdout: string, stderr: string, exitCode: number}>}
 */
function runPythonScript(scriptName, args = [], cwd = process.cwd()) {
  return new Promise((resolve) => {
    const scriptPath = join(__dirname, "scripts", scriptName);
    const child = spawn("python3", [scriptPath, ...args], {
      cwd,
      stdio: ["pipe", "pipe", "pipe"],
    });

    let stdout = "";
    let stderr = "";

    child.stdout.on("data", (data) => {
      stdout += data.toString();
    });

    child.stderr.on("data", (data) => {
      stderr += data.toString();
    });

    child.on("close", (exitCode) => {
      resolve({ stdout, stderr, exitCode: exitCode ?? 0 });
    });
  });
}

/**
 * OpenCode Plugin for Engineering Standards
 * Provides tools to install, update, and check engineering standards in downstream projects.
 */
export const Plugin = async (input) => {
  const { $ } = input;

  return {
    tool: {
      /**
       * Install engineering standards into a target project.
       */
      installStandards: tool({
        description:
          "Install engineering-standards into a downstream project. Creates docs, AGENTS.md, .opencode/, .claude/, .cursor/, or .github/ files based on selected profiles.",
        args: {
          target: tool.schema
            .string()
            .optional()
            .describe("Target project root directory (default: current directory)"),
          profiles: tool.schema
            .array(tool.schema.string())
            .optional()
            .describe("Profiles to install: core, opencode, claude, cursor, copilot (default: core + opencode)"),
          force: tool.schema
            .boolean()
            .optional()
            .describe("Overwrite conflicting existing files"),
        },
        async execute(args, context) {
          const target = args.target || ".";
          const profiles = args.profiles || ["core", "opencode"];
          const force = args.force || false;

          const scriptArgs = [
            "--target",
            target,
            ...profiles.flatMap((p) => ["--profile", p]),
          ];
          if (force) scriptArgs.push("--force");

          const result = await runPythonScript(
            "install_standards.py",
            scriptArgs,
            context.directory
          );

          if (result.exitCode !== 0) {
            return {
              output: `Installation failed:\n${result.stderr}`,
              metadata: { success: false, exitCode: result.exitCode },
            };
          }

          return {
            output: result.stdout,
            metadata: { success: true, profiles, target },
          };
        },
      }),

      /**
       * Update an existing engineering standards installation.
       */
      updateStandards: tool({
        description:
          "Update an existing engineering-standards installation in a target project. Preserves local changes unless --force is used.",
        args: {
          target: tool.schema
            .string()
            .optional()
            .describe("Target project root directory (default: current directory)"),
          profiles: tool.schema
            .array(tool.schema.string())
            .optional()
            .describe("Override installed profiles for this update"),
          force: tool.schema
            .boolean()
            .optional()
            .describe("Overwrite locally modified managed files"),
        },
        async execute(args, context) {
          const target = args.target || ".";
          const profiles = args.profiles;
          const force = args.force || false;

          const scriptArgs = ["--target", target];
          if (profiles) {
            scriptArgs.push(...profiles.flatMap((p) => ["--profile", p]));
          }
          if (force) scriptArgs.push("--force");

          const result = await runPythonScript(
            "update_standards.py",
            scriptArgs,
            context.directory
          );

          if (result.exitCode !== 0) {
            return {
              output: `Update failed:\n${result.stderr}`,
              metadata: { success: false, exitCode: result.exitCode },
            };
          }

          return {
            output: result.stdout,
            metadata: { success: true, target },
          };
        },
      }),

      /**
       * Check the status of an engineering standards installation.
       */
      checkStandardsStatus: tool({
        description:
          "Check whether engineering-standards is installed in a target project and show installed profiles/version.",
        args: {
          target: tool.schema
            .string()
            .optional()
            .describe("Target project root directory (default: current directory)"),
        },
        async execute(args, context) {
          const target = args.target || ".";
          const fs = await import("fs/promises");
          const path = await import("path");

          const manifestPath = path.resolve(context.directory, target, ".engineering-standards", "manifest.json");

          try {
            const manifestData = await fs.readFile(manifestPath, "utf-8");
            const manifest = JSON.parse(manifestData);

            return {
              output: `engineering-standards is installed:\n- Version: ${manifest.version || "unknown"}\n- Profiles: ${(manifest.profiles || []).join(", ")}\n- Installed: ${manifest.installed_at || "unknown"}\n- Source: ${manifest.source_revision || "unknown"}`,
              metadata: { installed: true, manifest },
            };
          } catch (err) {
            return {
              output: `engineering-standards is NOT installed in ${target}.\nRun installStandards to install it.`,
              metadata: { installed: false },
            };
          }
        },
      }),

      /**
       * Check if code changes comply with engineering standards.
       */
      checkStandardsCompliance: tool({
        description:
          "Check if current code changes comply with engineering standards (method length, class size, SOLID principles, test coverage).",
        args: {
          filePath: tool.schema
            .string()
            .optional()
            .describe("Path to file to check (optional)"),
        },
        async execute(args, context) {
          // TODO: Implement actual compliance checking by reading AGENTS.md/CODING_PRACTICES.md
          // and analyzing the file. For now, return a placeholder.
          return {
            output: `Compliance check placeholder.\nChecks: method-length, class-size, solid-principles, test-coverage.\nFile: ${args.filePath || "(all changes)"}`,
            metadata: {
              compliant: true,
              checks: ["method-length", "class-size", "solid-principles", "test-coverage"],
            },
          };
        },
      }),
    },

    /**
     * Auto-update check: when OpenCode initializes, check if the installed standards
     * are out of date and suggest an update.
     */
    event: async ({ event }) => {
      // Check for update on session start if standards are installed
      if (event.type === "session.start") {
        try {
          const fs = await import("fs/promises");
          const path = await import("path");
          const manifestPath = path.resolve(process.cwd(), ".engineering-standards", "manifest.json");
          
          let manifest;
          try {
            const data = await fs.readFile(manifestPath, "utf-8");
            manifest = JSON.parse(data);
          } catch {
            // Not installed, skip auto-update check
            return;
          }

          // Get current source version
          const sourceResult = await runPythonScript("standards_distribution.py", ["--version"], process.cwd());
          const currentVersion = sourceResult.stdout.trim();
          const installedVersion = manifest.version || "unknown";

          if (currentVersion !== installedVersion && currentVersion !== "unknown") {
            console.log(`[engineering-standards] Update available: ${installedVersion} → ${currentVersion}`);
            console.log(`[engineering-standards] Run 'updateStandards' to update.`);
          }
        } catch {
          // Silently fail auto-update check
        }
      }
    },
  };
};
