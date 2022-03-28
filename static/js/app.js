(function () {
    const header = document.getElementById('header')
    window.addEventListener('scroll', e => {
        header.style.height = `${Math.max(30, 70 - Math.min(document.body.scrollTop, 70))}px`
    })
})()
