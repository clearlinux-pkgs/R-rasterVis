#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rasterVis
Version  : 0.50.2
Release  : 43
URL      : https://cran.r-project.org/src/contrib/rasterVis_0.50.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rasterVis_0.50.2.tar.gz
Summary  : Visualization Methods for Raster Data
Group    : Development/Tools
License  : GPL-3.0
Requires: R-RColorBrewer
Requires: R-hexbin
Requires: R-latticeExtra
Requires: R-raster
Requires: R-sp
Requires: R-terra
Requires: R-viridisLite
Requires: R-zoo
BuildRequires : R-RColorBrewer
BuildRequires : R-hexbin
BuildRequires : R-latticeExtra
BuildRequires : R-raster
BuildRequires : R-sp
BuildRequires : R-terra
BuildRequires : R-viridisLite
BuildRequires : R-zoo
BuildRequires : buildreq-R

%description
[![CRAN](http://www.r-pkg.org/badges/version/rasterVis)](https://www.r-pkg.org/pkg/rasterVis)
[![CRAN RStudio mirror downloads](http://cranlogs.r-pkg.org/badges/rasterVis)](https://cran.r-project.org/package=rasterVis)
[![Build Status](https://github.com/oscarperpinan/rastervis/workflows/R-CMD-check/badge.svg)](https://github.com/oscarperpinan/rastervis/actions)

%prep
%setup -q -c -n rasterVis
cd %{_builddir}/rasterVis

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619999982

%install
export SOURCE_DATE_EPOCH=1619999982
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rasterVis || :


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
