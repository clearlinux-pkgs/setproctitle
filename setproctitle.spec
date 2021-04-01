#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6013BD3AFCF957DE (daniele.varrazzo@gmail.com)
#
Name     : setproctitle
Version  : 1.2.2
Release  : 35
URL      : https://files.pythonhosted.org/packages/a1/7f/a1d4f4c7b66f0fc02f35dc5c85f45a8b4e4a7988357a29e61c14e725ef86/setproctitle-1.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/a1/7f/a1d4f4c7b66f0fc02f35dc5c85f45a8b4e4a7988357a29e61c14e725ef86/setproctitle-1.2.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/a1/7f/a1d4f4c7b66f0fc02f35dc5c85f45a8b4e4a7988357a29e61c14e725ef86/setproctitle-1.2.2.tar.gz.asc
Summary  : A Python module to customize the process title
Group    : Development/Tools
License  : BSD-3-Clause
Requires: setproctitle-license = %{version}-%{release}
Requires: setproctitle-python = %{version}-%{release}
Requires: setproctitle-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
==============================================

%package license
Summary: license components for the setproctitle package.
Group: Default

%description license
license components for the setproctitle package.


%package python
Summary: python components for the setproctitle package.
Group: Default
Requires: setproctitle-python3 = %{version}-%{release}

%description python
python components for the setproctitle package.


%package python3
Summary: python3 components for the setproctitle package.
Group: Default
Requires: python3-core
Provides: pypi(setproctitle)

%description python3
python3 components for the setproctitle package.


%prep
%setup -q -n setproctitle-1.2.2
cd %{_builddir}/setproctitle-1.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617299774
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/setproctitle
cp %{_builddir}/setproctitle-1.2.2/COPYRIGHT %{buildroot}/usr/share/package-licenses/setproctitle/ad731867414c721228cfe9db129c47563dcc2cbe
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/setproctitle/ad731867414c721228cfe9db129c47563dcc2cbe

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
