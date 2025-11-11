import { defineConfig } from 'vitepress'
import mathjax3 from 'markdown-it-mathjax3'

// 自定义插件处理 mcreference 标签
function mcreferencePlugin(md) {
  // 在渲染之前处理原始文本
  md.core.ruler.before('normalize', 'mcreference', function(state) {
    const src = state.src
    const newSrc = src.replace(
      /<mcreference\s+link="([^"]+)"\s+index="([^"]+)">([^<]+)<\/mcreference>/g,
      '<sup><a href="$1" target="_blank" rel="noopener noreferrer" class="reference-link">[$2]</a></sup>'
    )
    state.src = newSrc
  })
}

export default defineConfig({
  title: '昆泰芯微电子 技术文档',
  description: '昆泰芯微电子 - 智能感知世界，传递美好生活',
  base: '/devsite/',
  ignoreDeadLinks: true,
  
  markdown: {
    config: (md) => {
      md.use(mathjax3)
      md.use(mcreferencePlugin)
    }
  },
  
  themeConfig: {
    logo: '/logo.jpg',
    siteTitle: false,
    
    // 启用浅色主题（默认）
    appearance: true, // true表示默认浅色主题，用户可以切换到深色
    
    nav: [
      { text: '首页', link: '/' },
      { 
        text: '产品系列', 
        items: [
          { text: 'KTH16xx系列', link: '/products/KTH16xx/' },
          { text: 'KTH17xx系列', link: '/products/KTH17xx/' },
          { text: 'KTH25xx系列', link: '/products/KTH25xx/' },
          { text: 'KTH31xx系列', link: '/products/KTH31xx/' },
          { text: 'KTH46xx系列', link: '/products/KTH46xx/' },
          { text: 'KTH56xx系列', link: '/products/KTH56xx/' },
          { text: 'KTH57xx系列', link: '/products/KTH57xx/' },
          { text: 'KTH78xx系列', link: '/products/KTH78xx/' },
          { text: 'KTM13xx系列', link: '/products/KTM13xx/' },
          { text: 'KTM58xx系列', link: '/products/KTM58xx/' },
          { text: 'KTAX333', link: '/products/KTAX333/' },
          { text: 'KTP112', link: '/products/KTP112/' }
        ]
      },
      { text: '应用中心', link: '/applications/' },
      { text: '技术百科', link: '/knowledge/' },
      { 
        text: '技术支持', 
        items: [
          { text: '技术文档', link: '/technical/' },
          { text: '资源下载', link: '/resources/' }
        ]
      }
    ],
    
    sidebar: {
      '/': [
        {
          text: '导航',
          items: [
            { text: '首页', link: '/' },
            { text: '应用中心', link: '/applications/' },
            { text: '技术百科', link: '/knowledge/' }
          ]
        },
        {
          text: '产品系列',
          collapsed: false,
          items: [
            { text: 'KTH16xx系列', link: '/products/KTH16xx/' },
            { text: 'KTH17xx系列', link: '/products/KTH17xx/' },
            { text: 'KTH25xx系列', link: '/products/KTH25xx/' },
            { text: 'KTH31xx系列', link: '/products/KTH31xx/' },
            { text: 'KTH46xx系列', link: '/products/KTH46xx/' },
            { text: 'KTH56xx系列', link: '/products/KTH56xx/' },
            { text: 'KTH57xx系列', link: '/products/KTH57xx/' },
            { text: 'KTH78xx系列', link: '/products/KTH78xx/' },
            { text: 'KTM13xx系列', link: '/products/KTM13xx/' },
            { text: 'KTM58xx系列', link: '/products/KTM58xx/' },
            { text: '其他传感器', link: '/products/other-sensors/' }
          ]
        },
        {
          text: '技术支持',
          collapsed: true,
          items: [
            { text: '技术文档', link: '/technical/' },
            { text: '资源下载', link: '/resources/' }
          ]
        }
      ],
      '/products/': [
        {
          text: '产品中心',
          items: [
            { text: '产品概览', link: '/products/' }
          ]
        },
        {
          text: '产品系列',
          items: [
            { text: 'KTH16xx系列', link: '/products/KTH16xx/' },
            { text: 'KTH17xx系列', link: '/products/KTH17xx/' },
            { text: 'KTH25xx系列', link: '/products/KTH25xx/' },
            { text: 'KTH31xx系列', link: '/products/KTH31xx/' },
            { text: 'KTH46xx系列', link: '/products/KTH46xx/' },
            { text: 'KTH56xx系列', link: '/products/KTH56xx/' },
            { text: 'KTH57xx系列', link: '/products/KTH57xx/' },
            { text: 'KTH78xx系列', link: '/products/KTH78xx/' },
            { text: 'KTM13xx系列', link: '/products/KTM13xx/' },
            { text: 'KTM58xx系列', link: '/products/KTM58xx/' },
            { text: 'KTAX333', link: '/products/KTAX333/' },
            { text: 'KTP112', link: '/products/KTP112/' }
          ]
        }
      ],
      '/products/KTH16xx/': [
        {
          text: 'KTH16xx系列',
          items: [
            { text: '系列概览', link: '/products/KTH16xx/' },
            { text: 'KTH1601', link: '/products/KTH16xx/KTH1601' },
            { text: 'KTH1601SL', link: '/products/KTH16xx/KTH1601SL' },
            { text: 'KTH1604', link: '/products/KTH16xx/KTH1604' },
            { text: 'KTH1604SM', link: '/products/KTH16xx/KTH1604SM' },
            { text: 'KTH1605P', link: '/products/KTH16xx/KTH1605P' },
            { text: 'KTH1611', link: '/products/KTH16xx/KTH1611' },
            { text: 'KTH1621', link: '/products/KTH16xx/KTH1621' },
            { text: 'KTH1631', link: '/products/KTH16xx/KTH1631' },
            { text: 'KTH1642', link: '/products/KTH16xx/KTH1642' }
          ]
        }
      ],
      '/products/KTH17xx/': [
        {
          text: 'KTH17xx系列',
          items: [
            { text: '系列概览', link: '/products/KTH17xx/' },
            { text: 'KTH1701', link: '/products/KTH17xx/KTH1701' },
            { text: 'KTH1702', link: '/products/KTH17xx/KTH1702' },
            { text: 'KTH1711', link: '/products/KTH17xx/KTH1711' },
            { text: 'KTH1721', link: '/products/KTH17xx/KTH1721' },
            { text: 'KTH1722', link: '/products/KTH17xx/KTH1722' }
          ]
        }
      ],
      '/products/KTH25xx/': [
        {
          text: 'KTH25xx系列',
          items: [
            { text: '系列概览', link: '/products/KTH25xx/' },
            { text: 'KTH2502', link: '/products/KTH25xx/KTH2502' },
            { text: 'KTH2582', link: '/products/KTH25xx/KTH2582' }
          ]
        }
      ],
      '/products/KTH31xx/': [
        {
          text: 'KTH31xx系列',
          items: [
            { text: '系列概览', link: '/products/KTH31xx/' },
            { text: 'KTH31XX', link: '/products/KTH31xx/KTH31XX' }
          ]
        }
      ],
      '/products/KTH46xx/': [
        {
          text: 'KTH46xx系列',
          items: [
            { text: '系列概览', link: '/products/KTH46xx/' },
            { text: 'KTH462N', link: '/products/KTH46xx/KTH462N' },
            { text: 'KTH462NXX', link: '/products/KTH46xx/KTH462NXX' },
            { text: 'KTH4603', link: '/products/KTH46xx/KTH4603' },
            { text: 'KTH4603XX', link: '/products/KTH46xx/KTH4603XX' }
          ]
        }
      ],
      '/products/KTH56xx/': [
        {
          text: 'KTH56xx系列',
          items: [
            { text: '系列概览', link: '/products/KTH56xx/' },
            { text: 'KTH5641', link: '/products/KTH56xx/KTH5641' },
            { text: 'KTH5642', link: '/products/KTH56xx/KTH5642' },
            { text: 'KTH5643', link: '/products/KTH56xx/KTH5643' },
            { text: 'KTH564A1', link: '/products/KTH56xx/KTH564A1' }
          ]
        }
      ],
      '/products/KTH57xx/': [
        {
          text: 'KTH57xx系列',
          items: [
            { text: '系列概览', link: '/products/KTH57xx/' },
            { text: 'KTH5701AQ1', link: '/products/KTH57xx/KTH5701AQ1' },
            { text: 'KTH5701AQ2', link: '/products/KTH57xx/KTH5701AQ2' },
            { text: 'KTH5702AQ1', link: '/products/KTH57xx/KTH5702AQ1' },
            { text: 'KTH5702AQ2', link: '/products/KTH57xx/KTH5702AQ2' },
            { text: 'KTH5761AQ3', link: '/products/KTH57xx/KTH5761AQ3' },
            { text: 'KTH5762AQ3', link: '/products/KTH57xx/KTH5762AQ3' },
            { text: 'KTH5763AQ3', link: '/products/KTH57xx/KTH5763AQ3' },
            { text: 'KTH5772', link: '/products/KTH57xx/KTH5772' },
            { text: 'KTH5774', link: '/products/KTH57xx/KTH5774' },
            { text: 'KTH5791AQ3', link: '/products/KTH57xx/KTH5791AQ3' }
          ]
        }
      ],
      '/products/KTH78xx/': [
        {
          text: 'KTH78xx系列',
          items: [
            { text: '系列概览', link: '/products/KTH78xx/' },
            { text: 'KTH7801', link: '/products/KTH78xx/KTH7801' },
            { text: 'KTH7812', link: '/products/KTH78xx/KTH7812' },
            { text: 'KTH7813', link: '/products/KTH78xx/KTH7813' },
            { text: 'KTH7814', link: '/products/KTH78xx/KTH7814' },
            { text: 'KTH7815', link: '/products/KTH78xx/KTH7815' },
            { text: 'KTH7816', link: '/products/KTH78xx/KTH7816' },
            { text: 'KTH7823', link: '/products/KTH78xx/KTH7823' },
            { text: 'KTH7824', link: '/products/KTH78xx/KTH7824' }
          ]
        }
      ],
      '/products/KTM13xx/': [
        {
          text: 'KTM13xx系列',
          items: [
            { text: '系列概览', link: '/products/KTM13xx/' },
            { text: 'KTM1301', link: '/products/KTM13xx/KTM1301' },
            { text: 'KTM1302', link: '/products/KTM13xx/KTM1302' },
            { text: 'KTM1302LTC', link: '/products/KTM13xx/KTM1302LTC' },
            { text: 'KTM1302R', link: '/products/KTM13xx/KTM1302R' },
            { text: 'KTM1304', link: '/products/KTM13xx/KTM1304' },
            { text: 'KTM1311', link: '/products/KTM13xx/KTM1311' },
            { text: 'KTM1321', link: '/products/KTM13xx/KTM1321' },
            { text: 'KTM1331', link: '/products/KTM13xx/KTM1331' },
            { text: 'KTM1331R', link: '/products/KTM13xx/KTM1331R' }
          ]
        }
      ],
      '/products/KTM58xx/': [
        {
          text: 'KTM58xx系列',
          items: [
            { text: '系列概览', link: '/products/KTM58xx/' },
            { text: 'KTM5800', link: '/products/KTM58xx/KTM5800' }
          ]
        }
      ],
      '/products/KTAX333/': [
        {
          text: 'KTAX333',
          items: [
            { text: '产品详情', link: '/products/KTAX333/' }
          ]
        }
      ],
      '/products/KTP112/': [
        {
          text: 'KTP112',
          items: [
            { text: '产品详情', link: '/products/KTP112/' }
          ]
        }
      ],
      '/products/KTH4603/': [
        {
          text: 'KTH4603',
          items: [
            { text: '产品详情', link: '/products/KTH4603/' }
          ]
        }
      ],
      '/products/KTH4603XX/': [
        {
          text: 'KTH4603XX',
          items: [
            { text: '产品详情', link: '/products/KTH4603XX/' }
          ]
        }
      ],
      '/technical/': [
        {
          text: '技术资料',
          items: [
            { text: '技术文档', link: '/technical/' },
            { text: 'PDF到Markdown转换指南', link: '/technical/pdf-to-markdown-guide' }
          ]
        }
      ],
      '/resources/': [
        {
          text: '资源下载',
          items: [
            { text: '资源中心', link: '/resources/' }
          ]
        }
      ],
      '/applications/': [
        {
          text: '应用中心',
          items: [
            { text: '应用概览', link: '/applications/' },
            { text: '工业自动化', link: '/applications/industrial-automation' },
            { text: '汽车电子', link: '/applications/automotive' },
            { text: '消费电子', link: '/applications/consumer-electronics' },
            { text: '新能源', link: '/applications/renewable-energy' }
          ]
        }
      ],
      '/knowledge/': [
        {
          text: '技术百科',
          items: [
            { text: '百科首页', link: '/knowledge/' },
            { text: '传感器基础', link: '/knowledge/sensor-basics' },
            { text: '电子技术', link: '/knowledge/electronics' },
            { text: '应用技术', link: '/knowledge/applications' },
            { text: '设计指南', link: '/knowledge/design-guide' },
            { text: '测试验证', link: '/knowledge/testing' },
            { text: '标准规范', link: '/knowledge/standards' }
          ]
        }
      ]
    },
    
    socialLinks: [
      { icon: 'github', link: 'https://github.com' }
    ],
    
    footer: {
      message: '昆泰芯微电子 - 智能感知世界，传递美好生活',
      copyright: 'Copyright © 2024 昆泰芯微电子'
    }
  }
})
