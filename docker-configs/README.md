# Docker配置文件说明

这个文件夹包含了所有Docker相关的配置文件，已经整理好供您使用。

## 推荐使用的文件（最简单）

### 1. 主要配置文件
- `docker-compose.yml` - 主要的Docker Compose配置文件（推荐使用）
- `nginx.conf` - Nginx配置文件

### 2. 使用方法
```bash
# 进入docker-configs目录
cd docker-configs

# 启动服务
docker-compose up -d

# 停止服务
docker-compose down
```

## 其他文件说明（可选）

- `docker-compose-permission-fix.yml` - 包含多种权限解决方案的示例文件
- `Dockerfile.nginx` - 自定义Nginx镜像的Dockerfile
- `docker-compose-simple-nginx.yml` - 原始的简单配置文件
- `nginx-simple.conf` - 原始的Nginx配置文件

## 建议

**只使用主要配置文件即可**，其他文件是为了展示不同的解决方案，您可以忽略或删除它们。

如果您觉得文件太多，可以删除以下文件：
- `docker-compose-permission-fix.yml`
- `docker-compose-simple-nginx.yml` 
- `nginx-simple.conf`
- `Dockerfile.nginx`

保留 `docker-compose.yml` 和 `nginx.conf` 即可。