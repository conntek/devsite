<script setup>
import { computed } from 'vue'
const modules = import.meta.glob('../../blog/*.md', { eager: true })
const posts = computed(() =>
  Object.entries(modules)
    .map(([path, mod]) => {
      const fm = mod.frontmatter || {}
      const href = path.replace('../../blog/', '/blog/').replace(/\.md$/, '')
      return { title: fm.title, date: fm.date, tags: fm.tags || [], href }
    })
    .filter(p => p.title && p.date)
    .sort((a, b) => new Date(b.date) - new Date(a.date))
)
</script>

<template>
  <div>
    <ul>
      <li v-for="p in posts" :key="p.href">
        <a :href="p.href">{{ p.title }}</a>
        <span> · {{ new Date(p.date).toLocaleDateString() }}</span>
      </li>
    </ul>
  </div>
  <div v-if="posts.length === 0">暂无文章</div>
</template>
