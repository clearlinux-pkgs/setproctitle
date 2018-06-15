#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6013BD3AFCF957DE (daniele.varrazzo@gmail.com)
#
Name     : setproctitle
Version  : 1.1.10
Release  : 11
URL      : http://pypi.debian.net/setproctitle/setproctitle-1.1.10.tar.gz
Source0  : http://pypi.debian.net/setproctitle/setproctitle-1.1.10.tar.gz
Source99 : http://pypi.debian.net/setproctitle/setproctitle-1.1.10.tar.gz.asc
Summary  : A Python module to customize the process title
Group    : Development/Tools
License  : BSD-3-Clause
Requires: setproctitle-python3
Requires: setproctitle-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
==============================================

%package legacypython
Summary: legacypython components for the setproctitle package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the setproctitle package.


%package python
Summary: python components for the setproctitle package.
Group: Default
Requires: setproctitle-python3

%description python
python components for the setproctitle package.


%package python3
Summary: python3 components for the setproctitle package.
Group: Default
Requires: python3-core

%description python3
python3 components for the setproctitle package.


%prep
%setup -q -n setproctitle-1.1.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519422712
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1519422712
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
