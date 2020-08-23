const iconTable = document.querySelector('table')
const iconDir = "icons"

window.onload = () => {
    createIcons()
}

function createIcons() {
    chrome.runtime.getPackageDirectoryEntry((root) => {
        root.getDirectory(iconDir, {create: false}, (dir) => {
            const reader = dir.createReader()
            reader.readEntries((results) => buildTable(results.map(r => r.name)))
        })
    })
}

function buildTable(imgNames) {
    for(let img of imgNames.sort()) {
        const iconRow = document.createElement('tr')
        
        const shortcutCell = document.createElement('td')
        const shortcut = document.createElement('span')
        shortcut.innerHTML = `<b>:${img.split('.png')[0]}:</b>`
        shortcutCell.append(shortcut)

        const iconCell = document.createElement('td')
        const icon = document.createElement('img')
        icon.src = chrome.extension.getURL(`/${iconDir}/${img}`)    
        icon.width = '61'
        iconCell.append(icon)
        
        iconRow.append(shortcutCell, iconCell)
        iconTable.append(iconRow)
    }
}