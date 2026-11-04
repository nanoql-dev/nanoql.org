// SPDX-FileCopyrightText: 2026 The nanoql Authors
// SPDX-License-Identifier: Apache-2.0

// The wordmark follows the colour mode: its dark form on dark pages. main.css swaps it at once where browsers let CSS
// replace an image; this covers the rest, and a change of mode after the page has loaded.
function followTheme() {
  const logo = document.getElementById('logo')
  if (!logo) return
  const light = logo.getAttribute('src')
  const dark = light.replace('nanoql-wordmark-light.svg', 'nanoql-wordmark-dark.svg')
  const apply = () => {
    logo.src = document.documentElement.getAttribute('data-bs-theme') === 'dark' ? dark : light
  }
  apply()
  new MutationObserver(apply).observe(document.documentElement, { attributes: true, attributeFilter: ['data-bs-theme'] })
}

export default {
  iconLinks: [
    { icon: 'github', href: 'https://github.com/nanoql-dev/nanoql', title: 'GitHub' }
  ],
  start: followTheme
}
