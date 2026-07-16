(function () {
  const base = document.body.dataset.base || '';
  const active = document.body.dataset.page || 'home';

  function href(path) {
    if (!path || path === '#') return '#';
    if (path.startsWith('http') || path.startsWith('mailto:') || path.startsWith('tel:')) return path;
    return base + path;
  }

  function asset(path) {
    return base + path;
  }

  const services = [
    { href: 'services/erp-services.html', label: 'ERP Services' },
    { href: 'services/application-managed-services.html', label: 'Application Managed Services' },
    { href: 'services/web-development.html', label: 'Web Development' },
    { href: 'services/mobile-applications.html', label: 'Mobile Applications' },
    { href: 'services/qa-testing.html', label: 'QA & Testing' },
  ];

  const practices = [
    { href: 'practices/workday.html', label: 'Workday' },
    { href: 'practices/sap.html', label: 'SAP' },
    { href: 'practices/salesforce.html', label: 'Salesforce' },
    { href: 'practices/oracle-cloud-applications.html', label: 'Oracle Cloud Applications' },
  ];

  function isActive(key) {
    return active === key ? 'text-primary' : 'text-dark hover:text-primary';
  }

  function dropdownItems(items) {
    return items
      .map(
        (item) =>
          `<a href="${href(item.href)}" class="block px-4 py-2 text-sm text-dark hover:text-primary hover:bg-gray-50">${item.label}</a>`
      )
      .join('');
  }

  function renderHeader() {
    const mount = document.getElementById('site-header');
    if (!mount) return;

    mount.innerHTML = `
<header class="relative z-40 bg-white">
  <div class="bg-white border-b border-gray-100">
    <div class="max-w-container mx-auto px-4">
      <div class="flex items-center justify-between min-h-[42px]">
        <div class="header-skew flex items-center pe-8 py-2 z-[1]">
          <div class="relative z-[1] flex items-center gap-4">
            <a href="tel:+18477224913" class="flex items-center gap-2 text-white text-sm font-semibold hover:opacity-90">
              <img src="${asset('assets/theme/icons/light-phone.svg')}" alt="" class="w-[22px] h-[22px]" onerror="this.style.display='none'" />
              +1 (847) 722-4913
            </a>
            <a href="mailto:info@applettek.com" class="hidden xl:flex items-center gap-2 text-white text-sm font-semibold hover:opacity-90">
              <img src="${asset('assets/theme/icons/light-email.svg')}" alt="" class="w-[22px] h-[22px]" onerror="this.style.display='none'" />
              info@applettek.com
            </a>
          </div>
        </div>
        <div class="flex items-center gap-4 ms-auto">
          <span class="hidden md:block text-dark text-xs lg:text-sm font-semibold whitespace-nowrap">
            Mon - Fri 9:00 AM - 5:00 PM / Sat 10:00 AM - 6:00 PM / Sunday - CLOSED
          </span>
          <div class="flex items-center gap-3 text-dark text-base">
            <a href="https://www.facebook.com/" target="_blank" rel="noopener" class="hover:text-primary" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
            <a href="https://www.linkedin.com/" target="_blank" rel="noopener" class="hover:text-primary" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
            <a href="https://www.instagram.com/" target="_blank" rel="noopener" class="hover:text-primary" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div id="main-nav-bar" class="sticky-header bg-white">
    <div class="max-w-container mx-auto px-4">
      <div class="flex items-center justify-between h-[100px] lg:h-[110px]">
        <a href="${href('index.html')}" class="shrink-0 py-1">
          <img src="${asset('assets/brand/logos/Applettek-logo.png')}" alt="APPLETTEK — AI Enabled. Future Ready." class="h-14 md:h-16 w-auto max-w-[220px] object-contain" />
        </a>

        <nav class="hidden lg:flex items-center gap-0.5 xl:gap-1">
          <a href="${href('index.html')}" class="px-2.5 py-2 text-[15px] font-medium capitalize ${isActive('home')}">Home</a>
          <a href="${href('about-us.html')}" class="px-2.5 py-2 text-[15px] font-medium capitalize ${isActive('about')}">About Us</a>
          <div class="relative group">
            <a href="${href('services/erp-services.html')}" class="px-2.5 py-2 text-[15px] font-medium capitalize inline-flex items-center gap-1 ${isActive('services')}">
              Services <i class="fas fa-chevron-down text-[10px]"></i>
            </a>
            <div class="invisible opacity-0 group-hover:visible group-hover:opacity-100 transition absolute top-full left-0 min-w-[260px] bg-white shadow-soft border-t-2 border-primary py-2 z-50">
              ${dropdownItems(services)}
            </div>
          </div>
          <div class="relative group">
            <a href="${href('practices/workday.html')}" class="px-2.5 py-2 text-[15px] font-medium capitalize inline-flex items-center gap-1 ${isActive('practices')}">
              Practices <i class="fas fa-chevron-down text-[10px]"></i>
            </a>
            <div class="invisible opacity-0 group-hover:visible group-hover:opacity-100 transition absolute top-full left-0 min-w-[240px] bg-white shadow-soft border-t-2 border-primary py-2 z-50">
              ${dropdownItems(practices)}
            </div>
          </div>
          <a href="${href('clients.html')}" class="px-2.5 py-2 text-[15px] font-medium capitalize ${isActive('clients')}">Clients</a>
          <a href="${href('careers.html')}" class="px-2.5 py-2 text-[15px] font-medium capitalize ${isActive('careers')}">Careers</a>
        </nav>

        <div class="flex items-center gap-3">
          <a href="${href('contact-us.html')}" class="btn-offset hidden lg:inline-flex bg-dark text-white text-sm font-semibold px-5 py-2.5">
            <span>Contact Us</span>
          </a>
          <button id="mobile-menu-btn" class="lg:hidden text-dark text-xl p-2" aria-label="Menu">
            <i class="fas fa-bars"></i>
          </button>
        </div>
      </div>
    </div>

    <div id="mobile-menu" class="hidden lg:hidden border-t border-gray-100 bg-white">
      <nav class="max-w-container mx-auto px-4 py-4 flex flex-col gap-1 text-sm">
        <a href="${href('index.html')}" class="py-2 font-medium ${isActive('home')}">Home</a>
        <a href="${href('about-us.html')}" class="py-2 font-medium ${isActive('about')}">About Us</a>
        <p class="pt-2 text-xs font-semibold tracking-wider text-grey uppercase">Services</p>
        ${services.map((s) => `<a href="${href(s.href)}" class="py-1.5 pl-3 text-dark hover:text-primary">${s.label}</a>`).join('')}
        <p class="pt-2 text-xs font-semibold tracking-wider text-grey uppercase">Practices</p>
        ${practices.map((p) => `<a href="${href(p.href)}" class="py-1.5 pl-3 text-dark hover:text-primary">${p.label}</a>`).join('')}
        <a href="${href('clients.html')}" class="py-2 font-medium ${isActive('clients')}">Clients</a>
        <a href="${href('careers.html')}" class="py-2 font-medium ${isActive('careers')}">Careers</a>
        <a href="${href('contact-us.html')}" class="py-2 font-medium ${isActive('contact')}">Contact Us</a>
      </nav>
    </div>
  </div>
  <div id="nav-spacer" class="hidden" style="height:100px"></div>
</header>`;
  }

  function renderFooter() {
    const mount = document.getElementById('site-footer');
    if (!mount) return;

    mount.innerHTML = `
<footer class="bg-cover bg-center text-gray-300" style="background-image: url('${asset('assets/theme/backgrounds/background-4.jpg')}');">
  <div class="max-w-container mx-auto px-4 pt-10">
    <div class="flex flex-col lg:flex-row justify-between items-start lg:items-center gap-6 py-10">
      <h2 class="font-semibold text-white text-3xl md:text-4xl mb-0">Applettek IT Consulting</h2>
      <a href="${href('contact-us.html')}" class="btn-offset inline-flex bg-primary text-white font-medium px-6 py-3 text-base">
        <span>Contact Us</span>
      </a>
    </div>
    <hr class="border-white/20" />
    <div class="grid md:grid-cols-2 lg:grid-cols-12 gap-8 pt-12 pb-8">
      <div class="lg:col-span-4">
        <a href="${href('index.html')}" class="inline-block bg-white rounded-md px-3 py-2 mb-4">
          <img src="${asset('assets/brand/logos/Applettek-logo.png')}" alt="APPLETTEK — AI Enabled. Future Ready." class="h-14 w-auto max-w-[200px] object-contain" />
        </a>
        <p class="text-base mb-5 leading-relaxed">IT consulting services encompass a wide range of expertise and assistance in leveraging technology to address business challenges and improve organizational efficiency.</p>
        <div class="flex gap-3">
          <a href="https://facebook.com" target="_blank" rel="noopener" class="w-10 h-10 border border-white/30 flex items-center justify-center text-white hover:border-primary hover:text-primary" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
          <a href="https://linkedin.com" target="_blank" rel="noopener" class="w-10 h-10 border border-white/30 flex items-center justify-center text-white hover:border-primary hover:text-primary" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
        </div>
      </div>
      <div class="lg:col-span-3 space-y-4">
        <h4 class="font-bold text-white text-lg mb-2">Contact Info</h4>
        <a href="tel:+18477224913" class="flex items-center gap-2 text-white font-semibold hover:text-primary">
          <i class="fas fa-phone text-primary"></i> +1 (847) 722-4913
        </a>
        <a href="mailto:info@applettek.com" class="flex items-center gap-2 text-white font-semibold hover:text-primary">
          <i class="fas fa-envelope text-primary"></i> info@applettek.com
        </a>
        <a href="mailto:hr@applettek.com" class="flex items-center gap-2 text-white font-semibold hover:text-primary">
          <i class="fas fa-envelope text-primary"></i> hr@applettek.com
        </a>
      </div>
      <div class="lg:col-span-2">
        <h4 class="font-bold text-white text-lg mb-4">Company</h4>
        <ul class="space-y-2 text-sm">
          <li><a href="${href('index.html')}" class="hover:text-primary">Home</a></li>
          <li><a href="${href('about-us.html')}" class="hover:text-primary">About Us</a></li>
          <li><a href="${href('privacy-policy.html')}" class="hover:text-primary">Privacy Policy</a></li>
          <li><a href="${href('testimonials.html')}" class="hover:text-primary">Testimonials</a></li>
          <li><a href="${href('contact-us.html')}" class="hover:text-primary">Contact Us</a></li>
        </ul>
      </div>
      <div class="lg:col-span-3">
        <h4 class="font-bold text-white text-lg mb-4">Working Hours</h4>
        <ul class="space-y-2 text-sm text-gray-300">
          <li>Mon - Fri : 9:00 AM - 5:00 PM</li>
          <li>Sat : 10:00 AM - 6:00 PM</li>
          <li>Sunday Closed</li>
        </ul>
      </div>
    </div>
    <div class="text-center pb-10">
      <hr class="border-white/20 mt-4 mb-6" />
      <p class="text-sm mb-0">Copyright 2026 - All Rights Reserved By <a href="https://alldgm.com/" class="text-white hover:text-primary">ALL DGM Solutions</a></p>
    </div>
  </div>
</footer>`;
  }

  function initInteractions() {
    const mobileBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    if (mobileBtn && mobileMenu) {
      mobileBtn.addEventListener('click', () => mobileMenu.classList.toggle('hidden'));
      mobileMenu.querySelectorAll('a').forEach((a) =>
        a.addEventListener('click', () => mobileMenu.classList.add('hidden'))
      );
    }

    const navBar = document.getElementById('main-nav-bar');
    const spacer = document.getElementById('nav-spacer');
    if (navBar && spacer) {
      window.addEventListener('scroll', () => {
        if (window.scrollY > 120) {
          if (!navBar.classList.contains('is-stuck')) {
            spacer.style.height = navBar.offsetHeight + 'px';
            spacer.classList.remove('hidden');
            navBar.classList.add('is-stuck');
          }
        } else {
          navBar.classList.remove('is-stuck');
          spacer.classList.add('hidden');
        }
      });
    }

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) e.target.classList.add('visible');
        });
      },
      { threshold: 0.12 }
    );
    document.querySelectorAll('.fade-up').forEach((el) => observer.observe(el));

    const progressSection = document.getElementById('progress-bars');
    if (progressSection) {
      const progressObserver = new IntersectionObserver(
        (entries) => {
          entries.forEach((e) => {
            if (e.isIntersecting) {
              e.target.querySelectorAll('.progress-bar-fill').forEach((bar) => {
                bar.style.width = bar.dataset.width;
              });
              progressObserver.unobserve(e.target);
            }
          });
        },
        { threshold: 0.3 }
      );
      progressObserver.observe(progressSection);
    }

    const slides = document.querySelectorAll('.testimonial-slide');
    const dotsWrap = document.getElementById('testimonial-dots');
    if (slides.length) {
      let tIndex = 0;
      if (dotsWrap) {
        slides.forEach((_, i) => {
          const btn = document.createElement('button');
          btn.className = 'carousel-dot' + (i === 0 ? ' active' : '');
          btn.setAttribute('aria-label', 'Slide ' + (i + 1));
          btn.addEventListener('click', () => showTestimonial(i));
          dotsWrap.appendChild(btn);
        });
      }
      function showTestimonial(i) {
        slides[tIndex].classList.add('hidden');
        if (dotsWrap && dotsWrap.children[tIndex]) dotsWrap.children[tIndex].classList.remove('active');
        tIndex = (i + slides.length) % slides.length;
        slides[tIndex].classList.remove('hidden');
        if (dotsWrap && dotsWrap.children[tIndex]) dotsWrap.children[tIndex].classList.add('active');
      }
      const prev = document.getElementById('testimonial-prev');
      const next = document.getElementById('testimonial-next');
      if (prev) prev.addEventListener('click', () => showTestimonial(tIndex - 1));
      if (next) next.addEventListener('click', () => showTestimonial(tIndex + 1));
    }

    const form = document.getElementById('contact-form');
    if (form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const success = document.getElementById('form-success');
        const error = document.getElementById('form-error');
        if (success) success.classList.remove('hidden');
        if (error) error.classList.add('hidden');
        form.reset();
      });
    }
  }

  renderHeader();
  renderFooter();
  initInteractions();
})();
