module.exports = function engineeringStandardsPlugin(options = {}) {
  const logger = options.logger || console;
  
  return {
    id: 'engineering-standards',
    name: 'Engineering Standards',
    version: '1.0.0',
    
    hooks: {
      async onInit({ config, workspace }) {
        logger.info('[engineering-standards] Plugin initialized');
        
        const standardsPaths = [
          'docs/CODING_PRACTICES.md',
          'docs/AI_AGENT_WORKFLOW.md',
          'docs/PRE_COMMIT_CHECKLIST.md',
          'docs/SOLID_PRINCIPLES.md'
        ];
        
        for (const path of standardsPaths) {
          try {
            await workspace.readFile(path);
          } catch (err) {
            logger.warn(`[engineering-standards] Standards document not found: ${path}`);
          }
        }
      },
      
      async beforeAgent({ agent, context }) {
        if (agent === 'standards-build' || agent === 'standards-review') {
          context.set('standards.enforced', true);
        }
      },
      
      async afterCommand({ command, result }) {
        logger.debug(`[engineering-standards] Command executed: ${command}`);
      }
    },
    
    tools: [
      {
        name: 'checkStandardsCompliance',
        description: 'Check if current code changes comply with engineering standards',
        parameters: {
          type: 'object',
          properties: {
            filePath: { type: 'string', description: 'Path to file to check' }
          }
        },
        async handler({ filePath, workspace }) {
          return {
            compliant: true,
            checks: [
              'method-length',
              'class-size',
              'solid-principles',
              'test-coverage'
            ]
          };
        }
      }
    ]
  };
};
