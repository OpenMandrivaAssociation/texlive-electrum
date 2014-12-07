# revision 19705
# category Package
# catalog-ctan /fonts/electrumadf
# catalog-date 2010-07-28 12:27:25 +0200
# catalog-license other-free
# catalog-version 1.005-b
Name:		texlive-electrum
Version:	1.005b
Release:	9
Summary:	Electrum ADF fonts collection
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/electrumadf
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/electrum.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/electrum.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/electrum.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Electrum ADF is a slab-serif font featuring optical and italic
small-caps; additional ligatures and an alternate Q; lining,
hanging, inferior and superior digits; and four weights. The
fonts are provided in Adobe Type 1 format and the support
material enables use with LaTeX. Licence is mixed: LPPL for
LaTeX support; GPL with font exception for the fonts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/arkandis/electrum/yesb8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/electrum/yesbo8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/electrum/yesl8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/electrum/yeslo8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/electrum/yesr8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/electrum/yesro8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/electrum/yess8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/electrum/yesso8a.afm
%{_texmfdistdir}/fonts/enc/dvips/electrum/supp-yes.enc
%{_texmfdistdir}/fonts/map/dvips/electrum/yes.map
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesb08c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesb08t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesb0o8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesb0o8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesb18c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesb18t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesb1o8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesb1o8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesb8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesb8r.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesb8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesb8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesbc8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesbcj8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesbcjo8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesbcjow8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesbcjw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesbco8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesbcow8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesbcw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesbj8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesbj8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesbjo8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesbjo8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesbjow8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesbjw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesbo8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesbo8r.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesbo8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesbo8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesbow8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesbw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesl08c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesl08t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesl0o8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesl0o8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesl18c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesl18t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesl1o8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesl1o8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesl8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesl8r.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesl8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesl8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yeslc8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yeslcj8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yeslcjo8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yeslcjow8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yeslcjw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yeslco8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yeslcow8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yeslcw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yeslj8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yeslj8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesljo8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesljo8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesljow8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesljw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yeslo8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yeslo8r.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yeslo8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yeslo8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yeslow8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yeslw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesr08c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesr08t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesr0o8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesr0o8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesr18c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesr18t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesr1o8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesr1o8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesr8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesr8r.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesr8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesr8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesrc8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesrcj8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesrcjo8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesrcjow8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesrcjw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesrco8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesrcow8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesrcw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesrj8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesrj8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesrjo8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesrjo8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesrjow8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesrjw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesro8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesro8r.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesro8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesro8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesrow8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesrw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yess08c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yess08t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yess0o8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yess0o8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yess18c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yess18t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yess1o8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yess1o8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yess8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yess8r.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yess8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yess8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yessc8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesscj8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesscjo8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesscjow8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesscjw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yessco8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesscow8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesscw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yessj8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yessj8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yessjo8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yessjo8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yessjow8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yessjw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesso8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesso8r.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesso8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yesso8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yessow8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/electrum/yessw8t.tfm
%{_texmfdistdir}/fonts/type1/arkandis/electrum/yesb8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/electrum/yesb8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/electrum/yesbo8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/electrum/yesbo8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/electrum/yesl8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/electrum/yesl8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/electrum/yeslo8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/electrum/yeslo8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/electrum/yesr8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/electrum/yesr8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/electrum/yesro8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/electrum/yesro8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/electrum/yess8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/electrum/yess8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/electrum/yesso8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/electrum/yesso8a.pfm
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesb08c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesb08t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesb0o8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesb0o8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesb18c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesb18t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesb1o8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesb1o8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesb8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesb8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesbc8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesbcj8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesbcjo8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesbcjow8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesbcjw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesbco8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesbcow8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesbcw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesbj8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesbj8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesbjo8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesbjo8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesbjow8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesbjw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesbo8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesbo8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesbow8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesbw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesl08c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesl08t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesl0o8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesl0o8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesl18c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesl18t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesl1o8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesl1o8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesl8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesl8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yeslc8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yeslcj8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yeslcjo8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yeslcjow8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yeslcjw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yeslco8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yeslcow8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yeslcw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yeslj8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yeslj8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesljo8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesljo8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesljow8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesljw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yeslo8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yeslo8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yeslow8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yeslw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesr08c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesr08t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesr0o8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesr0o8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesr18c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesr18t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesr1o8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesr1o8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesr8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesr8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesrc8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesrcj8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesrcjo8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesrcjow8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesrcjw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesrco8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesrcow8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesrcw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesrj8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesrj8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesrjo8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesrjo8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesrjow8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesrjw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesro8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesro8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesrow8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesrw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yess08c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yess08t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yess0o8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yess0o8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yess18c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yess18t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yess1o8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yess1o8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yess8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yess8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yessc8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesscj8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesscjo8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesscjow8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesscjw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yessco8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesscow8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesscw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yessj8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yessj8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yessjo8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yessjo8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yessjow8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yessjw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesso8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yesso8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yessow8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/electrum/yessw8t.vf
%{_texmfdistdir}/tex/latex/electrum/electrum.sty
%{_texmfdistdir}/tex/latex/electrum/t1yes.fd
%{_texmfdistdir}/tex/latex/electrum/t1yes0.fd
%{_texmfdistdir}/tex/latex/electrum/t1yes1.fd
%{_texmfdistdir}/tex/latex/electrum/t1yesj.fd
%{_texmfdistdir}/tex/latex/electrum/t1yesjw.fd
%{_texmfdistdir}/tex/latex/electrum/t1yesw.fd
%{_texmfdistdir}/tex/latex/electrum/ts1yes.fd
%{_texmfdistdir}/tex/latex/electrum/ts1yes0.fd
%{_texmfdistdir}/tex/latex/electrum/ts1yes1.fd
%{_texmfdistdir}/tex/latex/electrum/ts1yesj.fd
%{_texmfdistdir}/tex/latex/electrum/ts1yesjw.fd
%{_texmfdistdir}/tex/latex/electrum/ts1yesw.fd
%doc %{_texmfdistdir}/doc/fonts/electrum/COPYING
%doc %{_texmfdistdir}/doc/fonts/electrum/NOTICE.txt
%doc %{_texmfdistdir}/doc/fonts/electrum/README
%doc %{_texmfdistdir}/doc/fonts/electrum/electrumadf.pdf
%doc %{_texmfdistdir}/doc/fonts/electrum/electrumadf.tex
%doc %{_texmfdistdir}/doc/fonts/electrum/manifest.txt
#- source
%doc %{_texmfdistdir}/source/fonts/electrum/build-ttsc.mtx
%doc %{_texmfdistdir}/source/fonts/electrum/dotsc2.etx
%doc %{_texmfdistdir}/source/fonts/electrum/dotscbuild.mtx
%doc %{_texmfdistdir}/source/fonts/electrum/dotscmisc.mtx
%doc %{_texmfdistdir}/source/fonts/electrum/newlatin-dotsc.mtx
%doc %{_texmfdistdir}/source/fonts/electrum/reglyph-yes.tex
%doc %{_texmfdistdir}/source/fonts/electrum/supp-yes.etx
%doc %{_texmfdistdir}/source/fonts/electrum/t1-dotinferior.etx
%doc %{_texmfdistdir}/source/fonts/electrum/t1-dotsuperior.etx
%doc %{_texmfdistdir}/source/fonts/electrum/t1-yes.etx
%doc %{_texmfdistdir}/source/fonts/electrum/t1-yesw-sc.etx
%doc %{_texmfdistdir}/source/fonts/electrum/t1-yesw.etx
%doc %{_texmfdistdir}/source/fonts/electrum/t1j-yes.etx
%doc %{_texmfdistdir}/source/fonts/electrum/t1j-yesw-sc.etx
%doc %{_texmfdistdir}/source/fonts/electrum/t1j-yesw.etx
%doc %{_texmfdistdir}/source/fonts/electrum/ts1-dotinferior.etx
%doc %{_texmfdistdir}/source/fonts/electrum/ts1-dotoldstyle-yes.etx
%doc %{_texmfdistdir}/source/fonts/electrum/ts1-dotsuperior.etx
%doc %{_texmfdistdir}/source/fonts/electrum/ts1-yes.etx
%doc %{_texmfdistdir}/source/fonts/electrum/yes-drv.tex
%doc %{_texmfdistdir}/source/fonts/electrum/yes-map.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.005b-2
+ Revision: 751403
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.005b-1
+ Revision: 718318
- texlive-electrum
- texlive-electrum
- texlive-electrum

