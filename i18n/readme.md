echo "切换到python语义化工具"
cd /d C:\Program Files\Python37\Tools\i18n
echo "扫描gettex_()标记的py 生成 pot"
python pygettext.py -o D:\study\python_demo\i18n\locale\resource.pot D:\study\python_demo\i18n\i18n.py
echo "创建翻译文件目录"
mkdir D:\study\python_demo\i18n\locale\
mkdir D:\study\python_demo\i18n\locale\en-US\LC_MESSAGES
mkdir D:\study\python_demo\i18n\locale\zh-CN\LC_MESSAGES
echo "拷贝pot到对应语言"
COPY  D:\study\python_demo\i18n\locale\resource.pot D:\study\python_demo\i18n\locale\zh-CN\LC_MESSAGES\resource.po D:\study\python_demo\i18n\locale\en-US\LC_MESSAGES\resource.po
echo "翻译对应po成mo"
python msgfmt.py -o D:\study\python_demo\i18n\locale\en-US\LC_MESSAGES\resource.mo D:\study\python_demo\i18n\locale\en-US\LC_MESSAGES\resource.po
python msgfmt.py -o D:\study\python_demo\i18n\locale\zh-CH\LC_MESSAGES\resource.mo D:\study\python_demo\i18n\locale\zh-CH\LC_MESSAGES\resource.po