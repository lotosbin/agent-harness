const pptxgen = require('pptxgenjs');
const path = require('path');
const html2pptx = require('/Users/liubinbin/.claude/plugins/cache/anthropic-agent-skills/document-skills/69c0b1a06741/skills/pptx/scripts/html2pptx.js');
async function createPresentation() {
    const pptx = new pptxgen();
    pptx.layout = 'LAYOUT_16x9';
    pptx.author = 'Superpowers';
    pptx.title = 'Superpowers 快速入门';
    pptx.subject = 'AI 编码助手工作流';
    const slidesDir = path.join(__dirname, 'slides');
    const slideFiles = [
        'slide01-title.html',
        'slide02-problem.html',
        'slide03-what.html',
        'slide04-install.html',
        'slide05-workflow.html',
        'slide06-tdd.html',
        'slide07-comparison.html',
        'slide08-next.html'
    ];
    for (const file of slideFiles) {
        const htmlPath = path.join(slidesDir, file);
        console.log(`Processing: ${file}`);
        await html2pptx(htmlPath, pptx);
    }
    const outputPath = path.join(__dirname, 'Superpowers-Quickstart.pptx');
    await pptx.writeFile({ fileName: outputPath });
    console.log(`Created: ${outputPath}`);
}
createPresentation().catch(err => {
    console.error('Error:', err);
    process.exit(1);
});
