# VitePress Webhook 自动部署 Docker 配置

这个配置提供了一个完整的 VitePress 自动部署解决方案，使用多个专门的 Docker 容器来处理不同的功能，包括 webhook 接收、Git 同步、项目构建和 Web 服务。

## 前置要求

在开始部署之前，请确保您的系统已安装以下软件：

### Windows 系统
1. **Docker Desktop for Windows**
   - 下载地址：https://www.docker.com/products/docker-desktop/
   - 安装完成后重启系统
   - 确保Docker Desktop正在运行

2. **验证安装**
   ```powershell
   # 检查Docker是否安装成功
   docker --version
   docker compose version
   ```

### Linux 系统
1. **安装Docker**
   ```bash
   # Ubuntu/Debian
   sudo apt update
   sudo apt install docker.io docker-compose-plugin
   
   # CentOS/RHEL
   sudo yum install docker docker-compose-plugin
   
   # 启动Docker服务
   sudo systemctl start docker
   sudo systemctl enable docker
   ```

2. **添加用户到docker组**
   ```bash
   sudo usermod -aG docker $USER
   # 重新登录或重启系统使更改生效
   ```

### macOS 系统
1. **Docker Desktop for Mac**
   - 下载地址：https://www.docker.com/products/docker-desktop/
   - 安装并启动Docker Desktop

**注意：** 如果您的系统尚未安装Docker，请先完成Docker安装后再继续以下步骤。

## 架构设计

本方案采用超级一体化架构，包含以下容器：

- 🚀 **all-in-one**: 超级一体化服务，基于nginx的全功能容器
  - **Nginx**: Web服务器和反向代理
  - **Node.js**: Webhook接收和处理
  - **Git**: 代码同步功能
  - **VitePress**: 静态站点构建和预览
  - **Supervisor**: 进程管理和监控

### 超级一体化架构优势

- **终极简化**：所有功能集成到单个nginx容器中，部署极其简单
- **统一管理**：所有服务在同一容器中，便于监控和维护
- **资源最优**：最大化资源共享，最小化资源消耗
- **高性能**：本地通信，无网络延迟
- **自动化流程**：容器启动时自动克隆仓库并执行首次构建
- **定期同步**：每5分钟自动同步代码，确保内容最新
- **即时构建**：接收到webhook时立即同步代码并重新构建
- **进程监控**：Supervisor确保所有服务稳定运行

## 功能特性

- 🚀 **分离式架构**: 每个服务职责单一，易于维护和扩展
- 🔄 **自动同步**: Git 服务定期同步代码，确保数据一致性
- 📱 **VitePress 预览**: 专门的构建服务，支持实时预览
- 🔐 **安全验证**: 支持 webhook 签名验证
- 💾 **数据持久化**: 所有数据存储在当前目录下
- 🏥 **健康检查**: 内置健康检查和监控
- 🌐 **反向代理**: Nginx 提供统一的访问入口

## 快速开始

### 1. 配置环境变量

编辑 `docker-compose.yml` 文件中的环境变量：

```yaml
environment:
  - WEBHOOK_SECRET=KT2024_VitePress_AutoDeploy_Secure_Key_9f8e7d6c5b4a3210  # 实际的webhook密钥
  - GIT_REPO_URL=http://nashugo:3000/hugo/conntek.git  # 实际的Git仓库地址
```

### 2. 启动服务

```bash
# 启动超级一体化服务
docker compose up -d

# 查看日志
docker compose logs -f all-in-one

# 查看服务状态
docker compose ps

# 停止服务
docker compose down
```

### 3. 验证部署

```bash
# 检查主站点
curl -I http://nashugo/

# 检查API健康状态
curl http://nashugo/api/health

# 检查内部服务状态
docker exec all-in-one supervisorctl status
```

### 3. 配置Gitea Webhook

在Gitea仓库设置中添加webhook：

- **URL**: `http://nashugo/api/webhook`
- **Content Type**: `application/json`
- **Secret**: 与docker-compose.yml中的WEBHOOK_SECRET相同
- **Events**: 选择 "Push events"

## 端口配置

- **80**: 主Web服务端口（nginx）
  - `/`: VitePress静态站点
  - `/api/webhook`: 接收Git推送事件
  - `/api/build`: 手动触发构建
- **3001**: 内部Webhook API服务（通过nginx代理）
- **4173**: 内部VitePress预览服务（通过nginx代理）

## 服务端点

### 超级一体化服务 (all-in-one)

- **主站点**: `http://localhost/`
  - VitePress构建的静态站点
  - 通过nginx直接提供服务

- **Webhook接收**: `http://localhost/api/webhook`
  - 接收GitHub/GitLab的推送事件
  - 自动触发代码同步和构建

- **手动构建**: `http://localhost/api/build`
  - POST请求手动触发项目构建
  - 返回构建状态和结果

### API端点表格
| 端点 | 方法 | 描述 |
|------|------|------|
| `/` | GET | VitePress静态站点首页 |
| `/api/webhook` | POST | 接收Git推送事件的Webhook |
| `/api/build` | POST | 手动触发构建 |
| `/api/health` | GET | 健康检查 |

## 使用示例

### 健康检查
```bash
# 通过超级一体化服务检查
curl http://nashugo/api/health
```

### 手动触发构建
```bash
# 通过超级一体化服务触发
curl -X POST http://nashugo/api/build
```

### 访问网站
```bash
# 访问主站点
http://nashugo/
```

### 测试 Webhook
```bash
# 直接测试
curl -X POST http://nashugo:3001/webhook \
  -H "Content-Type: application/json" \
  -d '{"ref":"refs/heads/main","repository":{"clone_url":"http://nashugo:3000/hugo/conntek.git"}}'

# 通过代理测试
curl -X POST http://nashugo:8080/api/webhook \
  -H "Content-Type: application/json" \
  -d '{"ref":"refs/heads/main","repository":{"clone_url":"http://nashugo:3000/hugo/conntek.git"}}'
```

## 目录结构

部署后的目录结构：

```
项目根目录/
├── docker-compose.yml     # Docker Compose配置文件
├── nginx.conf            # Nginx配置文件
├── data/                 # 数据持久化目录（所有容器共享）
│   └── repo/            # Git仓库克隆目录
│       ├── docs/        # VitePress文档源码
│       ├── package.json # 项目依赖配置
│       └── ...          # 其他项目文件
└── logs/                # 日志文件目录
    ├── webhook.log      # Webhook服务日志
    ├── build.log        # 构建服务日志
    └── git-sync.log     # Git同步日志
```

## 工作流程

### 自动化流程
1. **Git同步**：git-sync容器每5分钟自动同步Git仓库
2. **接收Webhook**：webhook-server接收Gitea推送事件
3. **验证签名**：验证webhook签名确保安全性
4. **触发构建**：webhook-server通知vitepress-builder开始构建
5. **项目构建**：vitepress-builder安装依赖并构建项目
6. **启动预览**：构建完成后自动启动预览服务器
7. **代理访问**：通过Nginx统一代理访问各种服务

### 服务间通信
- webhook-server → vitepress-builder：HTTP API调用触发构建
- git-sync → 共享数据卷：定期同步代码到共享存储
- nginx → 各服务：反向代理统一访问入口

## 故障排除

### 常见问题

1. **飞牛NAS Docker环境特殊配置**

   **环境说明：**
   飞牛NAS内嵌Docker环境可能存在以下特殊情况：
   - 容器启动顺序问题
   - 网络配置限制
   - 资源分配限制
   - 存储卷权限问题

   **故障排除步骤：**
   1. 检查容器状态：在飞牛NAS Docker管理界面查看所有容器状态
   2. 查看容器日志：重点检查git-sync和nginx-proxy的启动日志
   3. 验证网络连通性：确保容器间网络通信正常
   4. 检查存储卷：确认./data和./logs目录权限正确

   **常见解决方案：**
   - 手动重启未启动的容器
   - 调整容器启动顺序（先启动git-sync，再启动其他服务）
   - 检查飞牛NAS的Docker网络配置
   - 确保有足够的系统资源（内存、CPU）
   - 创建.env文件设置环境变量
   - 避免外部文件挂载，使用内联配置

2. **Docker未安装或配置问题**
   ```powershell
   # Windows PowerShell - 检查Docker是否安装
   docker --version
   docker compose version
   
   # 如果提示"无法将'docker'项识别为cmdlet"，说明Docker未安装
   # 请参考上方"前置要求"部分安装Docker Desktop
   ```
   
   **解决方案：**
   - 确保Docker Desktop已安装并正在运行
   - 重启Docker Desktop服务
   - 检查Windows服务中的Docker服务是否启动
   - 确保当前用户有权限访问Docker

2. **环境变量未正确传递**
   ```bash
   # 检查git-sync容器日志，如果看到"You must specify a repository to clone"
   docker compose logs git-sync
   ```
   
   **解决方案：**
   - 检查docker-compose.yml中的环境变量配置
   - 确保GIT_REPO_URL变量正确设置
   - 重新启动服务：`docker compose down && docker compose up -d`

3. **Docker Compose字符串插值错误**
   
   **错误信息：**
   ```
   invalid interpolation format for services.xxx.command.
   You may need to escape any $ with another $.
   ```
   
   **解决方案：**
   在 `docker-compose.yml` 文件的 `command` 部分，所有JavaScript模板字符串中的 `${}` 需要转义为 `$${}：
   
   ```yaml
   # 错误写法
   console.log(`Server running on port ${PORT}`);
   
   # 正确写法
   console.log(`Server running on port $${PORT}`);
   ```
   
   **修复步骤：**
    1. 打开 `docker-compose.yml` 文件
    2. 找到所有包含 `${变量名}` 的行
    3. 将 `${变量名}` 替换为 `$${变量名}`
    4. 保存文件并重新启动服务

   **技术原因：**
   Docker Compose在解析YAML文件时会尝试进行变量替换，遇到`${}`格式会认为是环境变量引用。使用`$$`可以转义这个行为。

### 3. 环境变量未设置警告

**错误信息：**
```
The "GIT_REPO_URL" variable is not set. Defaulting to a blank string.
The "GIT_BRANCH" variable is not set. Defaulting to a blank string.
```

**解决方案：**
在项目根目录创建`.env`文件，设置所需的环境变量。

**修复步骤：**
1. 在docker-compose.yml同级目录创建`.env`文件
2. 添加必要的环境变量：
   ```
   GIT_REPO_URL=http://nashugo:3000/hugo/conntek.git
   GIT_BRANCH=main
   WEBHOOK_SECRET=your_secret_key
   NODE_ENV=production
   ```
3. 重新运行Docker Compose

### 4. 文件挂载错误

**错误信息：**
```
error mounting "/path/to/nginx.conf" to rootfs: cannot create subdirectories
Are you trying to mount a directory onto a file (or vice-versa)?
```

**解决方案：**
避免挂载外部配置文件，改用容器内生成配置的方式。

**修复步骤：**
1. 移除volumes中的配置文件挂载
2. 使用command字段在容器启动时生成配置
3. 确保挂载的目录存在且权限正确

**技术原因：**
飞牛NAS的Docker环境对文件挂载有特殊限制，外部文件挂载可能失败。使用内联配置可以避免这个问题。

**注意：**
- 项目目录中的`nginx.conf`文件现在仅作为参考，不会被Docker容器使用
- 实际的nginx配置是在容器启动时动态生成的
- 如需修改nginx配置，请编辑docker-compose.yml中nginx服务的command部分

### Git同步问题

**错误信息：**
```
Git sync failed: Command failed
```

**原因：**
1. Git仓库URL不可访问
2. 网络连接问题
3. 认证失败（如果仓库需要认证）

**解决方案：**
1. 检查`.env`文件中的`GIT_REPO_URL`是否正确
2. 确保Docker容器能访问Git服务器
3. 如需认证，配置SSH密钥或访问令牌

**修复步骤：**
```bash
# 检查容器日志
docker logs all-in-one

# 测试网络连接
docker exec all-in-one ping nashugo

# 手动测试git clone
docker exec all-in-one git clone http://nashugo:3000/hugo/conntek.git /tmp/test
```

3. **容器启动失败**
   ```bash
   # 查看所有容器状态
   docker compose ps
   
   # 查看特定容器日志
 docker compose logs all-in-one
   ```

2. **Webhook接收失败**
   - 检查防火墙设置，确保80端口开放
   - 验证Gitea webhook配置中的URL和密钥
   - 查看webhook服务日志：`docker compose logs -f all-in-one`
   - 检查服务状态：`docker compose exec all-in-one supervisorctl status`

3. **Git同步失败**
   - 检查Git仓库URL是否正确且可访问
   - 验证网络连接：`docker compose logs all-in-one`
   - 检查数据卷权限：`docker compose exec all-in-one ls -la /data`

4. **构建失败**
   - 检查VitePress配置：`docker compose exec all-in-one cat /app/data/repo/package.json`
   - 验证依赖安装：`docker compose exec all-in-one ls -la /app/data/repo/node_modules`
   - 手动触发构建：`curl -X POST http://localhost/api/build`
   - 查看构建服务日志：`docker compose logs -f all-in-one`
   - 检查Node.js版本兼容性

5. **预览服务无法访问**
   - 确保80端口没有被其他服务占用
   - 检查Nginx代理配置：`docker compose logs all-in-one`
   - 验证VitePress构建是否成功完成

### 调试命令

```bash
# 进入容器调试
docker compose exec all-in-one sh

# 查看容器资源使用
docker stats

# 重启服务
docker compose restart all-in-one

# 查看容器网络
docker network ls
docker network inspect $(docker compose ps -q | head -1 | xargs docker inspect --format='{{range .NetworkSettings.Networks}}{{.NetworkID}}{{end}}')

# 检查内部服务状态
docker compose exec all-in-one supervisorctl status
```

## 安全建议

1. **设置强密码**：修改 `WEBHOOK_SECRET` 为复杂密码
2. **网络隔离**：在生产环境中使用防火墙限制访问
3. **HTTPS配置**：在生产环境中配置HTTPS和SSL证书
4. **定期更新**：定期更新Docker镜像和依赖包
5. **访问控制**：限制webhook端点的访问来源
6. **日志监控**：定期检查日志文件，监控异常活动

## 自定义配置

### 修改环境变量

编辑 `docker-compose.yml` 中的环境变量：

```yaml
# webhook-server 服务
environment:
  - WEBHOOK_SECRET=KT2024_VitePress_AutoDeploy_Secure_Key_9f8e7d6c5b4a3210
  - GIT_REPO_URL=http://nashugo:3000/hugo/conntek.git
  - GIT_BRANCH=main

# git-sync 服务
environment:
  - GIT_REPO_URL=http://nashugo:3000/hugo/conntek.git
  - GIT_BRANCH=main
```

### 修改端口映射

如果需要使用不同的端口：

```yaml
# webhook-server
ports:
  - "8080:3000"  # 将webhook端口改为8080

# vitepress-builder
ports:
  - "8081:4173"  # 将预览端口改为8081

# nginx
ports:
  - "80:80"      # 使用标准HTTP端口
```

### 自定义Nginx配置

修改 `nginx.conf` 文件来自定义反向代理规则：

```nginx
# 添加SSL支持
server {
    listen 443 ssl;
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    # ... 其他配置
}

# 添加缓存配置
location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```

### 调整Git同步频率

修改 `git-sync` 服务的同步间隔：

```yaml
command: |
  sh -c '
    while true; do
      # ... git sync logic ...
      sleep 60  # 改为每1分钟同步一次
    done
  '
```

### 添加数据备份

可以添加备份服务来定期备份数据：

```yaml
backup:
  image: alpine:latest
  volumes:
    - ./data:/data:ro
    - ./backups:/backups
  command: |
    sh -c '
      while true; do
        tar -czf /backups/backup-$(date +%Y%m%d-%H%M%S).tar.gz /data
        find /backups -name "backup-*.tar.gz" -mtime +7 -delete
        sleep 86400  # 每天备份一次
      done
    '
```

## 生产环境部署建议

1. **使用外部数据库**：考虑使用外部Git服务和数据库
2. **负载均衡**：在高流量环境中使用多个构建服务实例
3. **监控告警**：集成Prometheus、Grafana等监控工具
4. **日志聚合**：使用ELK Stack或类似工具聚合日志
5. **自动扩缩容**：使用Kubernetes等容器编排工具

---

**注意**：
- 首次启动时，git-sync会自动克隆仓库，vitepress-builder会执行初始构建
- 整个过程可能需要几分钟时间，请耐心等待
- 建议在生产环境中使用具体的镜像版本标签而不是latest
- 所有数据都存储在当前目录的 `data` 和 `logs` 文件夹中

## 监控和日志

### 查看实时日志
```bash
# 查看所有服务日志
docker compose logs -f

# 查看特定服务日志
docker compose logs -f all-in-one

# 查看最近的日志（最后100行）
docker compose logs --tail=100 all-in-one
```

### 监控容器状态
```bash
# 查看容器状态
docker compose ps

# 查看资源使用情况
docker stats

# 查看容器详细信息
docker compose exec all-in-one ps aux
docker compose exec all-in-one df -h
```

### 健康检查
```bash
# 检查所有服务健康状态
curl http://nashugo/api/health  # 通过nginx代理

# 检查网站是否正常
curl -I http://nashugo/  # 访问主站点

# 检查内部服务状态
docker compose exec all-in-one supervisorctl status
```

### 性能监控
```bash
# 查看容器网络流量
docker exec all-in-one cat /proc/net/dev

# 查看磁盘使用情况
du -sh ./data ./logs

# 查看Git仓库大小
du -sh ./data/repo
```

### 日志文件说明

容器提供了详细的日志输出，包括：
- Webhook接收日志
- Git操作日志
- 构建过程日志
- 服务器启动日志
- Nginx访问日志

所有日志都可以通过 `docker compose logs` 命令查看，也会保存在 `./logs/` 目录中。

---

这个多容器配置提供了一个完整、可扩展的VitePress自动部署解决方案。通过微服务架构，每个组件都有明确的职责，便于维护和扩展。使用Docker Compose，你可以轻松管理整个部署流程，实现真正的一键部署。