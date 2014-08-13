#!/bin/bash
set -e
python setup.py bdist_rpm --spec-only --requires "supervisord, pika>=0.9.13" 
# The rpm needs to know about the .pyc and .pyo files. Kind of annoying, want to fix, patches welcome.
sed -i 's@%files -f INSTALLED_FILES@%files -f INSTALLED_FILES\n/etc/shove/settings.pyc\n/etc/shove/settings.pyo\n@' dist/shove.spec
# Another bug in bdist_rpm. Comas are going poof
sed -i 's/Requires: supervisord pika>=0.9.13/Requires: supervisord, pika>=0.9.13/' dist/shove.spec
rpmbuild -ba --define "_topdir ${PWD}/build/bdist.linux-x86_64/rpm" dist/shove.spec

cp build/bdist.linux-x86_64/rpm/RPMS/noarch/shove-0.1.4-1.noarch.rpm .

# Make a deb
fpm -s rpm -t deb build/bdist.linux-x86_64/rpm/RPMS/noarch/shove-0.1.4-1.noarch.rpm 
