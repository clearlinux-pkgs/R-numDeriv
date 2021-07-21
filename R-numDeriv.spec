#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-numDeriv
Version  : 2016.8.1.1
Release  : 33
URL      : https://cran.r-project.org/src/contrib/numDeriv_2016.8-1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/numDeriv_2016.8-1.1.tar.gz
Summary  : Accurate Numerical Derivatives
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
numerical first and second order derivatives. Accurate calculations 
	are done using 'Richardson''s' extrapolation or, when applicable, a
	complex step derivative is available. A simple difference 
	method is also provided. Simple difference is (usually) less accurate
	but is much quicker than 'Richardson''s' extrapolation and provides a 
	useful cross-check. 
	Methods are provided for real scalar and vector valued functions.

%prep
%setup -q -c -n numDeriv
cd %{_builddir}/numDeriv

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589511908

%install
export SOURCE_DATE_EPOCH=1589511908
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library numDeriv
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library numDeriv
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library numDeriv
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc numDeriv || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/numDeriv/DESCRIPTION
/usr/lib64/R/library/numDeriv/INDEX
/usr/lib64/R/library/numDeriv/Meta/Rd.rds
/usr/lib64/R/library/numDeriv/Meta/features.rds
/usr/lib64/R/library/numDeriv/Meta/hsearch.rds
/usr/lib64/R/library/numDeriv/Meta/links.rds
/usr/lib64/R/library/numDeriv/Meta/nsInfo.rds
/usr/lib64/R/library/numDeriv/Meta/package.rds
/usr/lib64/R/library/numDeriv/Meta/vignette.rds
/usr/lib64/R/library/numDeriv/NAMESPACE
/usr/lib64/R/library/numDeriv/NEWS
/usr/lib64/R/library/numDeriv/R/numDeriv
/usr/lib64/R/library/numDeriv/R/numDeriv.rdb
/usr/lib64/R/library/numDeriv/R/numDeriv.rdx
/usr/lib64/R/library/numDeriv/doc/Guide.R
/usr/lib64/R/library/numDeriv/doc/Guide.Stex
/usr/lib64/R/library/numDeriv/doc/Guide.pdf
/usr/lib64/R/library/numDeriv/doc/index.html
/usr/lib64/R/library/numDeriv/help/AnIndex
/usr/lib64/R/library/numDeriv/help/aliases.rds
/usr/lib64/R/library/numDeriv/help/numDeriv.rdb
/usr/lib64/R/library/numDeriv/help/numDeriv.rdx
/usr/lib64/R/library/numDeriv/help/paths.rds
/usr/lib64/R/library/numDeriv/html/00Index.html
/usr/lib64/R/library/numDeriv/html/R.css
/usr/lib64/R/library/numDeriv/tests/BWeg.R
/usr/lib64/R/library/numDeriv/tests/CSD.R
/usr/lib64/R/library/numDeriv/tests/grad01.R
/usr/lib64/R/library/numDeriv/tests/hessian01.R
/usr/lib64/R/library/numDeriv/tests/jacobian01.R
/usr/lib64/R/library/numDeriv/tests/oneSided.R
/usr/lib64/R/library/numDeriv/tests/trig01.R
