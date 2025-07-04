git init
git remote add origin http://192.168.0.203/root/speech-text.git
git add .
git config --global user.email "zhiwu.yin@xxx"
git config --global user.name "root"
git commit -m "Initial commit"
git push -u origin master  # 如果默认分支是 main，则使用 'main' 而不是 'master'
git push http://root:xxx@192.168.0.203/root/speech-text.git
git push http://root:xxx@192.168.0.203/root/speech-text.git


cd /d D:\Projects
git clone http://root:xx@192.168.0.203/root/video-crawler.git
cd video-crawler
git remote add origin http://root:xx@192.168.0.203/root/video-crawler.git
git fetch origin
git branch -a
git checkout -b master --track origin/master
git checkout master
git reset --hard origin/master


# 切换到 master 分支（如果有）
git checkout master

# 如果没有本地 master 分支，从远程创建一个
git checkout -b master --track origin/master

# 更新远程仓库信息
git fetch origin

# 查看远程和本地分支状态
git branch -a

# 合并远程 master 分支到本地
git pull origin master

# 解决任何可能出现的冲突（如果有的话）

# 验证同步状态
git log --oneline --graph --all


# 切换到目标目录
cd /d D:\Projects

# 克隆远程仓库，包含默认分支（通常是 main 或 master）
git clone http://root:your-token@192.168.0.203/root/video-crawler.git

# 进入克隆下来的项目目录
cd video-crawler

# 查看所有本地和远程分支，确认默认分支名称
git branch -a

# 如果默认分支是 main，而不是 master，请根据实际情况调整分支名称
# 假设你需要的是 master 分支：
if [ ! "$(git rev-parse --abbrev-ref HEAD)" = "master" ]; then
    # 创建并切换到 master 分支，跟踪远程的 origin/master
    git checkout -b master --track origin/master
fi

# 确保本地 master 分支与远程同步（如果有需要）
# 注意：仅当确定没有未提交的重要更改时使用此命令
git reset --hard origin/master


# 检查当前状态
git status

# 添加所有更改到暂存区
git add .

# 提交更改
git commit -m "Add new feature and fix bugs"

# 推送更改到远程仓库的 master 分支
git push origin master


# 切换到 master 分支（如果有）
git checkout master

# 如果没有本地 master 分支，从远程创建一个
git checkout -b master --track origin/master

# 更新远程仓库信息
git fetch origin

# 查看远程和本地分支状态
git branch -a

# 合并远程 master 分支到本地
git pull origin master

# 解决任何可能出现的冲突（如果有的话）

# 验证同步状态
git log --oneline --graph --all

git remote set-url origin http://root:your-personal-access-token@192.168.0.203/root/speech-text.git

git rm --cached path/to/example.txt

# 删除所有已追踪的 __pycache__ 内容
git rm -r --cached "**/__pycache__"

# 提交更改
git commit -m "Remove __pycache__ files from git tracking"
