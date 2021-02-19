#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sphinxcontrib-htmlhelp
Version  : 1.0.3
Release  : 18
URL      : https://files.pythonhosted.org/packages/c9/2e/a7a5fef38327b7f643ed13646321d19903a2f54b0a05868e4bc34d729e1f/sphinxcontrib-htmlhelp-1.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/c9/2e/a7a5fef38327b7f643ed13646321d19903a2f54b0a05868e4bc34d729e1f/sphinxcontrib-htmlhelp-1.0.3.tar.gz
Summary  : sphinxcontrib-htmlhelp is a sphinx extension which renders HTML help files
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sphinxcontrib-htmlhelp-license = %{version}-%{release}
Requires: sphinxcontrib-htmlhelp-python = %{version}-%{release}
Requires: sphinxcontrib-htmlhelp-python3 = %{version}-%{release}
Requires: flake8
Requires: mypy
BuildRequires : buildreq-distutils3
BuildRequires : flake8
BuildRequires : mypy
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
sphinxcontrib-htmlhelp is a sphinx extension which renders HTML help files.

%package license
Summary: license components for the sphinxcontrib-htmlhelp package.
Group: Default

%description license
license components for the sphinxcontrib-htmlhelp package.


%package python
Summary: python components for the sphinxcontrib-htmlhelp package.
Group: Default
Requires: sphinxcontrib-htmlhelp-python3 = %{version}-%{release}

%description python
python components for the sphinxcontrib-htmlhelp package.


%package python3
Summary: python3 components for the sphinxcontrib-htmlhelp package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib_htmlhelp)

%description python3
python3 components for the sphinxcontrib-htmlhelp package.


%prep
%setup -q -n sphinxcontrib-htmlhelp-1.0.3
cd %{_builddir}/sphinxcontrib-htmlhelp-1.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603404850
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
mkdir -p %{buildroot}/usr/share/package-licenses/sphinxcontrib-htmlhelp
cp %{_builddir}/sphinxcontrib-htmlhelp-1.0.3/LICENSE %{buildroot}/usr/share/package-licenses/sphinxcontrib-htmlhelp/7477e3e4ce73d4501e4086813a0d88b153ab4423
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinxcontrib-htmlhelp/7477e3e4ce73d4501e4086813a0d88b153ab4423

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
