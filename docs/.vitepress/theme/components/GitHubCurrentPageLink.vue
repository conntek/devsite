<script setup>
import { computed } from 'vue'
import { useData, useRoute } from 'vitepress'

const route = useRoute()
const { page, site } = useData()

const docPath = computed(() => {
  if (page.value?.relativePath) return page.value.relativePath
  const raw = route.path.split('#')[0].split('?')[0]
  let normalized = raw.endsWith('.html') ? raw.slice(0, -5) : raw
  const base = site.value.base || '/'
  if (base !== '/' && normalized.startsWith(base)) {
    normalized = `/${normalized.slice(base.length)}`
  }
  if (!normalized.endsWith('/')) normalized += '/'
  if (normalized === '/') return 'index.md'
  return `${normalized.slice(1)}index.md`
})

const encodedDocPath = computed(() => {
  return docPath.value
    .split('/')
    .map((segment) => encodeURIComponent(segment))
    .join('/')
})

const href = computed(() => {
  return `https://github.com/conntek/devsite/blob/main/docs/${encodedDocPath.value}`
})
</script>

<template>
  <a
    class="current-md-github"
    :href="href"
    target="_blank"
    rel="noreferrer"
    aria-label="查看当前页面 Markdown"
    title="查看当前页面 Markdown"
  >
    <svg viewBox="0 0 24 24" aria-hidden="true">
      <path d="M12 .5C5.65.5.5 5.65.5 12c0 5.08 3.29 9.39 7.86 10.91.57.1.78-.25.78-.56v-1.95c-3.2.7-3.88-1.36-3.88-1.36-.52-1.32-1.27-1.67-1.27-1.67-1.03-.7.08-.68.08-.68 1.15.08 1.75 1.18 1.75 1.18 1 .1 1.66.8 2.03 1.24.1-.76.4-1.28.72-1.58-2.55-.3-5.23-1.27-5.23-5.67 0-1.25.45-2.28 1.17-3.08-.12-.3-.5-1.52.12-3.17 0 0 .96-.3 3.14 1.18A10.95 10.95 0 0 1 12 6.3c.98 0 1.97.13 2.9.38 2.18-1.48 3.14-1.18 3.14-1.18.62 1.65.24 2.87.12 3.17.73.8 1.17 1.83 1.17 3.08 0 4.4-2.68 5.37-5.24 5.66.42.37.78 1.08.78 2.2v3.27c0 .31.2.67.78.56A11.5 11.5 0 0 0 23.5 12C23.5 5.65 18.35.5 12 .5Z"/>
    </svg>
  </a>
</template>
