import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import GitHubCurrentPageLink from './components/GitHubCurrentPageLink.vue'
import PostsList from './components/PostsList.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout: () => {
    return h(DefaultTheme.Layout, null, {
      'nav-bar-content-after': () => h(GitHubCurrentPageLink)
    })
  },
  enhanceApp({ app }) {
    app.component('PostsList', PostsList)
  }
}
