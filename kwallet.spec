#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kwallet
Version  : 5.60.0
Release  : 19
URL      : https://download.kde.org/stable/frameworks/5.60/kwallet-5.60.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.60/kwallet-5.60.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.60/kwallet-5.60.0.tar.xz.sig
Summary  : Secure and unified container for user passwords
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1
Requires: kwallet-bin = %{version}-%{release}
Requires: kwallet-data = %{version}-%{release}
Requires: kwallet-lib = %{version}-%{release}
Requires: kwallet-license = %{version}-%{release}
Requires: kwallet-locales = %{version}-%{release}
Requires: kwallet-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : docbook-xml
BuildRequires : gpgme
BuildRequires : gpgme-dev
BuildRequires : libgcrypt-dev
BuildRequires : libxml2
BuildRequires : libxml2-dev
BuildRequires : libxslt
BuildRequires : libxslt-dev
BuildRequires : qtbase-dev mesa-dev

%description
This directory consists of one daemon: kwalletd, and one library, in backend.
KWallet::Backend is used inside kwalletd to manage the actual files and
encryption.

%package bin
Summary: bin components for the kwallet package.
Group: Binaries
Requires: kwallet-data = %{version}-%{release}
Requires: kwallet-license = %{version}-%{release}

%description bin
bin components for the kwallet package.


%package data
Summary: data components for the kwallet package.
Group: Data

%description data
data components for the kwallet package.


%package dev
Summary: dev components for the kwallet package.
Group: Development
Requires: kwallet-lib = %{version}-%{release}
Requires: kwallet-bin = %{version}-%{release}
Requires: kwallet-data = %{version}-%{release}
Provides: kwallet-devel = %{version}-%{release}
Requires: kwallet = %{version}-%{release}
Requires: kwallet = %{version}-%{release}

%description dev
dev components for the kwallet package.


%package lib
Summary: lib components for the kwallet package.
Group: Libraries
Requires: kwallet-data = %{version}-%{release}
Requires: kwallet-license = %{version}-%{release}

%description lib
lib components for the kwallet package.


%package license
Summary: license components for the kwallet package.
Group: Default

%description license
license components for the kwallet package.


%package locales
Summary: locales components for the kwallet package.
Group: Default

%description locales
locales components for the kwallet package.


%package man
Summary: man components for the kwallet package.
Group: Default

%description man
man components for the kwallet package.


%prep
%setup -q -n kwallet-5.60.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1563063956
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1563063956
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kwallet
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kwallet/COPYING.LIB
cp src/runtime/kwallet-query/COPYING.LIB %{buildroot}/usr/share/package-licenses/kwallet/src_runtime_kwallet-query_COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang kwallet-query
%find_lang kwalletd5

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kwallet-query
/usr/bin/kwalletd5

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/kf5_org.kde.KWallet.xml
/usr/share/dbus-1/services/org.kde.kwalletd.service
/usr/share/dbus-1/services/org.kde.kwalletd5.service
/usr/share/knotifications5/kwalletd.notifyrc
/usr/share/kservices5/kwalletd5.desktop
/usr/share/qlogging-categories5/kwallet.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KWallet/KWallet
/usr/include/KF5/KWallet/kwallet.h
/usr/include/KF5/KWallet/kwallet_export.h
/usr/include/KF5/kwallet_version.h
/usr/lib64/cmake/KF5Wallet/KF5WalletConfig.cmake
/usr/lib64/cmake/KF5Wallet/KF5WalletConfigVersion.cmake
/usr/lib64/cmake/KF5Wallet/KF5WalletTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Wallet/KF5WalletTargets.cmake
/usr/lib64/libKF5Wallet.so
/usr/lib64/libkwalletbackend5.so
/usr/lib64/qt5/mkspecs/modules/qt_KWallet.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Wallet.so.5
/usr/lib64/libKF5Wallet.so.5.60.0
/usr/lib64/libkwalletbackend5.so.5
/usr/lib64/libkwalletbackend5.so.5.60.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kwallet/COPYING.LIB
/usr/share/package-licenses/kwallet/src_runtime_kwallet-query_COPYING.LIB

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/kwallet-query.1

%files locales -f kwallet-query.lang -f kwalletd5.lang
%defattr(-,root,root,-)

