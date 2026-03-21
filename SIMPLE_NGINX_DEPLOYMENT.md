# 简单 Nginx Docker 部署指南

这是一个简化的 Nginx Docker 配置，用于手动部署静态网站文件。

## 文件说明

- `docker-compose-simple-nginx.yml` - Docker Compose 配置文件
- `nginx-simple.conf` - Nginx 配置文件
- `dist/` - 静态文件目录（需要手动创建并复制文件）

## 使用步骤

### 1. 准备静态文件

首先构建你的 VitePress 项目：

```bash
npm run docs:build
```

### 2. 复制文件到 dist 目录

手动将构建后的文件复制到 `dist` 目录：

```bash
# 创建 dist 目录
mkdir dist

# 复制构建文件（根据你的构建输出目录调整）
cp -r docs/.vitepress/dist/* dist/
# 或者在 Windows 中：
# xcopy docs\.vitepress\dist\* dist\ /E /I
```

### 3. 启动服务

使用 Docker Compose 启动 Nginx 服务：

```bash
docker-compose -f docker-compose-simple-nginx.yml up -d
```

### 4. 访问网站

打开浏览器访问：
- 主站点：http://localhost/
- 健康检查：http://localhost/health

## 更新网站内容

当需要更新网站内容时：

1. 重新构建项目：
   ```bash
   npm run docs:build
   ```

2. 复制新文件到 dist 目录：
   ```bash
   # 清空旧文件
   rm -rf dist/*
   # 复制新文件
   cp -r docs/.vitepress/dist/* dist/
   ```

3. 重启容器（可选，Nginx 会自动读取新文件）：
   ```bash
   docker-compose -f docker-compose-simple-nginx.yml restart
   ```

## 管理命令

### 查看服务状态
```bash
docker-compose -f docker-compose-simple-nginx.yml ps
```

### 查看日志
```bash
docker-compose -f docker-compose-simple-nginx.yml logs -f nginx
```

### 停止服务
```bash
docker-compose -f docker-compose-simple-nginx.yml down
```

### 重启服务
```bash
docker-compose -f docker-compose-simple-nginx.yml restart
```

## 配置特性

- **静态文件缓存**：CSS、JS、图片等静态资源缓存 1 年
- **HTML 不缓存**：确保内容更新及时生效
- **Gzip 压缩**：减少传输大小，提高加载速度
- **安全头**：基本的安全防护
- **健康检查**：`/health` 端点用于监控
- **SPA 路由支持**：支持单页应用的路由

## 故障排除

### 1. 端口被占用
如果 80 端口被占用，修改 `docker-compose-simple-nginx.yml` 中的端口映射：
```yaml
ports:
  - "8080:80"  # 改为 8080 端口
```

### 2. 文件权限问题（403 Forbidden错误）
确保 `dist` 目录有正确的读取权限：
```bash
chmod -R 755 dist/
```

**在Docker Compose yml文件中解决权限问题的方案：**
   
   **方案1: 使用root用户运行（推荐）**
   ```yaml
   services:
     nginx:
       user: "0:0"  # 以root用户运行
   ```
   
   **方案2: 容器启动时修改权限**
   ```yaml
   services:
     nginx:
       command: >
         sh -c "chmod -R 755 /usr/share/nginx/html &&
                chown -R nginx:nginx /usr/share/nginx/html &&
                nginx -g 'daemon off;'"
   ```
   
   **方案3: 使用环境变量**
   ```yaml
   services:
     nginx:
       environment:
         - NGINX_USER=root
         - NGINX_GROUP=root
   ```
   
   **方案4: 使用自定义Dockerfile**
   ```yaml
   services:
     nginx:
       build:
         context: .
         dockerfile: Dockerfile.nginx
   ```
   
   项目中提供了完整的权限解决方案示例文件：
   - `docker-compose-permission-fix.yml` - 多种权限解决方案
   - `Dockerfile.nginx` - 自定义镜像方案

### 3. 容器无法启动
检查配置文件语法：
```bash
nginx -t -c /path/to/nginx-simple.conf
```

### 4. 网站无法访问
检查容器状态和日志：
```bash
docker-compose -f docker-compose-simple-nginx.yml ps
docker-compose -f docker-compose-simple-nginx.yml logs nginx
```

## 优势

- **简单易用**：只需复制文件即可部署
- **轻量级**：只包含 Nginx，资源占用少
- **高性能**：Nginx 静态文件服务性能优异
- **灵活性**：可以手动控制部署时机
- **兼容性**：支持任何静态网站项目

这个配置适合简单的静态网站部署需求，如果需要自动化部署功能，请使用完整的一体化方案。