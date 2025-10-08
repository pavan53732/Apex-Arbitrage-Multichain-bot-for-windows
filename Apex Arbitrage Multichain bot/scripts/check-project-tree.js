const fs = require('fs');
const path = require('path');

// Function to extract content between markers
function extractBetweenMarkers(content, startMarker, endMarker) {
  const startIndex = content.indexOf(startMarker);
  if (startIndex === -1) return null;
  const endIndex = content.indexOf(endMarker, startIndex + startMarker.length);
  if (endIndex === -1) return null;
  return content.substring(startIndex + startMarker.length, endIndex).trim();
}

// Function to extract top-level tree from PROJECT TREE COMPLETE STUCTURE .md
function extractTopLevelTree(treeContent) {
  const lines = treeContent.split('\n');
  let inTree = false;
  const treeLines = [];
  for (let line of lines) {
    // Skip initial empty lines
    if (!inTree && line.trim() === 'Apex Arbitrage Multichain bot/') {
      inTree = true;
      treeLines.push(line.trim());
      continue;
    }
    if (inTree) {
      // Stop when we reach a line that's not part of the tree structure
      if (line.match(/^[ª+|---]/) || line.trim() === '') {
        treeLines.push(line.trim());
      } else {
        break;
      }
    }
  }
  return treeLines.join('\n').trim();
}

async function main() {
  try {
    // Read README.md
    const readmePath = path.join(__dirname, '../README.md');
    const readmeContent = fs.readFileSync(readmePath, 'utf8');

    // Extract synced tree from README
    const syncedTree = extractBetweenMarkers(readmeContent, '<!-- BEGIN: SYNCED_PROJECT_TREE -->', '<!-- END: SYNCED_PROJECT_TREE -->');
    if (!syncedTree) {
      console.error('SYNCED_PROJECT_TREE block not found in README.md');
      process.exit(1);
    }

    // Read PROJECT TREE COMPLETE STUCTURE .md
    const treePath = path.join(__dirname, '../PROJECT TREE COMPLETE STUCTURE .md');
    const treeContent = fs.readFileSync(treePath, 'utf8');

    // Extract top-level tree
    const canonicalTree = extractTopLevelTree(treeContent);
    if (!canonicalTree) {
      console.error('Could not extract top-level tree from PROJECT TREE COMPLETE STUCTURE .md');
      process.exit(1);
    }

    // Compare
    if (syncedTree.trim() !== canonicalTree.trim()) {
      console.error('Project tree in README.md does not match canonical tree in PROJECT TREE COMPLETE STUCTURE .md');
      console.error('Synced tree:\n', syncedTree);
      console.error('Canonical tree:\n', canonicalTree);
      process.exit(1);
    } else {
      console.log('Project tree synchronization check passed!');
    }
  } catch (error) {
    console.error('Error during check:', error);
    process.exit(1);
  }
}

main();