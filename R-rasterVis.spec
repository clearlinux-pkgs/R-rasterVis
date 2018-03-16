#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rasterVis
Version  : 0.43
Release  : 1
URL      : https://cran.r-project.org/src/contrib/rasterVis_0.43.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rasterVis_0.43.tar.gz
Summary  : Visualization Methods for Raster Data
Group    : Development/Tools
License  : GPL-3.0
Requires: R-RColorBrewer
Requires: R-hexbin
Requires: R-latticeExtra
Requires: R-raster
Requires: R-viridisLite
Requires: R-zoo
BuildRequires : R-RColorBrewer
BuildRequires : R-hexbin
BuildRequires : R-latticeExtra
BuildRequires : R-raster
BuildRequires : R-viridisLite
BuildRequires : R-zoo
BuildRequires : clr-R-helpers

%description
[![CRAN](http://www.r-pkg.org/badges/version/rasterVis)](http://www.r-pkg.org/pkg/rasterVis)
[![CRAN RStudio mirror downloads](http://cranlogs.r-pkg.org/badges/rasterVis)](http://www.r-pkg.org/pkg/rasterVis)
[![Build Status](https://travis-ci.org/oscarperpinan/rastervis.svg?branch=master)](https://travis-ci.org/oscarperpinan/rastervis)
[![Research software impact](http://depsy.org/api/package/cran/rasterVis/badge.svg)](http://depsy.org/package/r/rasterVis)

%prep
%setup -q -c -n rasterVis

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521172871

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521172871
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rasterVis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rasterVis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rasterVis
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library rasterVis|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rasterVis/CITATION
/usr/lib64/R/library/rasterVis/DESCRIPTION
/usr/lib64/R/library/rasterVis/INDEX
/usr/lib64/R/library/rasterVis/Meta/Rd.rds
/usr/lib64/R/library/rasterVis/Meta/features.rds
/usr/lib64/R/library/rasterVis/Meta/hsearch.rds
/usr/lib64/R/library/rasterVis/Meta/links.rds
/usr/lib64/R/library/rasterVis/Meta/nsInfo.rds
/usr/lib64/R/library/rasterVis/Meta/package.rds
/usr/lib64/R/library/rasterVis/NAMESPACE
/usr/lib64/R/library/rasterVis/R/rasterVis
/usr/lib64/R/library/rasterVis/R/rasterVis.rdb
/usr/lib64/R/library/rasterVis/R/rasterVis.rdx
/usr/lib64/R/library/rasterVis/help/AnIndex
/usr/lib64/R/library/rasterVis/help/aliases.rds
/usr/lib64/R/library/rasterVis/help/paths.rds
/usr/lib64/R/library/rasterVis/help/rasterVis.rdb
/usr/lib64/R/library/rasterVis/help/rasterVis.rdx
/usr/lib64/R/library/rasterVis/html/00Index.html
/usr/lib64/R/library/rasterVis/html/R.css
