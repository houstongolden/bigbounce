# Tech Stack: BigBounce Research Paper

## Overview

The BigBounce project uses a minimal, academic-focused tech stack optimized for presenting theoretical physics research. The architecture prioritizes simplicity, reliability, and mathematical rendering capabilities over complex features.

## Core Technologies

### Frontend Framework
- **Framework**: Vanilla HTML/CSS/JavaScript
- **Rationale**: No complex state management needed, maximum compatibility
- **Version**: HTML5, CSS3, ES6+
- **Pattern**: Progressive enhancement

### Mathematical Rendering
- **Library**: MathJax 3.x
- **Provider**: CDN.js (Cloudflare)
- **Features**: LaTeX rendering, responsive equations, accessibility
- **Configuration**: Custom MathJax settings in `index.html`
- **Fallback**: Polyfill.io for ES6 support

### Development Server
- **Framework**: Express.js 5.1.0
- **Purpose**: Local development and testing
- **Port**: 3000 (configurable)
- **Features**: Static file serving, minimal overhead

### Deployment Platform
- **Provider**: Netlify
- **Configuration**: `netlify.toml`
- **Features**: Global CDN, automatic HTTPS, security headers
- **Build**: No build process required

## Library Dependencies

### Production Dependencies
```json
{
  "express": "^5.1.0"
}
```

### CDN Dependencies
- **MathJax**: `https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js`
- **Polyfill**: `https://polyfill.io/v3/polyfill.min.js?features=es6`

### No Build Dependencies
- **Package Managers**: None (minimal npm usage)
- **Bundlers**: None (direct file serving)
- **Transpilers**: None (modern browser support)
- **CSS Preprocessors**: None (vanilla CSS)

## Technology Patterns

### Content Management
- **Format**: Markdown with LaTeX
- **Organization**: File-based structure (`paper/` directory)
- **Version Control**: Git-based content tracking
- **No CMS**: Direct file editing workflow

### Asset Management
- **Images**: PNG format, direct file serving
- **Data**: Excel spreadsheets, direct download
- **Optimization**: Manual optimization, no automated pipeline
- **CDN**: Netlify automatic asset optimization

### Responsive Design
- **Approach**: Mobile-first design
- **Layout**: Flexbox-based responsive grid
- **Breakpoints**: Standard mobile/tablet/desktop
- **Typography**: Responsive font sizing

## Recommended Conventions

### HTML Structure
```html
<!-- Semantic HTML5 elements -->
<article class="research-paper">
  <header class="paper-header">
    <h1>Title</h1>
    <p class="author">Author</p>
  </header>
  
  <nav class="table-of-contents">
    <!-- Navigation structure -->
  </nav>
  
  <main class="paper-content">
    <!-- Content sections -->
  </main>
</article>
```

### CSS Organization
```css
/* Reset and base styles */
* { margin: 0; padding: 0; box-sizing: border-box; }

/* Typography */
body { font-family: 'Times New Roman', serif; }

/* Layout components */
.container { display: flex; }

/* Responsive breakpoints */
@media (max-width: 768px) { /* Mobile styles */ }
```

### JavaScript Patterns
```javascript
// Module pattern for organization
const BigBounce = {
  auth: {
    checkPassword: function(password) { /* ... */ },
    setAuthenticated: function() { /* ... */ }
  },
  
  navigation: {
    smoothScroll: function(target) { /* ... */ },
    highlightSection: function(section) { /* ... */ }
  },
  
  math: {
    configureMathJax: function() { /* ... */ },
    handleErrors: function(error) { /* ... */ }
  }
};
```

### Mathematical Expressions
```latex
<!-- Inline math -->
The Hubble constant $H_0 = 68.1 \pm 0.4$ km s$^{-1}$ Mpc$^{-1}$

<!-- Display math -->
$$\Lambda(t) = \Lambda_0 \left(\frac{a_0}{a(t)}\right)^4 = \Lambda_0 (1+z)^4$$
```

## Development Workflow

### Local Development
```bash
# Install dependencies
npm install

# Start development server
node server.js

# Access application
open http://localhost:3000
```

### Content Updates
1. Edit Markdown files in `paper/` directory
2. Update `index.html` to sync with content changes
3. Add images to `public/images/`
4. Update data files in `public/spreadsheets/`

### Deployment
```bash
# Git-based deployment
git add .
git commit -m "Update content"
git push origin main

# Automatic Netlify deployment
# No build process required
```

## Performance Considerations

### Loading Optimization
- **MathJax**: Loaded asynchronously
- **Images**: Progressive loading with lightbox
- **CSS**: Inline critical styles, external non-critical
- **JavaScript**: Minimal, non-blocking scripts

### Caching Strategy
```toml
# netlify.toml caching configuration
[[headers]]
  for = "/public/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000"
```

### Asset Optimization
- **Images**: Manual PNG optimization
- **CSS**: Minified in production
- **JavaScript**: Minimal code, no minification needed
- **MathJax**: CDN caching and compression

## Browser Support

### Target Browsers
- **Chrome**: 90+
- **Firefox**: 88+
- **Safari**: 14+
- **Edge**: 90+

### Feature Support
- **ES6 Modules**: Full support
- **Flexbox**: Full support
- **CSS Grid**: Partial support (fallback to flexbox)
- **MathJax**: Full support

### Fallbacks
- **JavaScript Disabled**: Basic HTML content
- **MathJax Failed**: Raw LaTeX display
- **CSS Failed**: Basic styling
- **Images Failed**: Alt text display

## Security Considerations

### Client-Side Security
- **Password Protection**: Cosmetic only (visible in source)
- **No Sensitive Data**: All content is public
- **XSS Protection**: Content sanitization
- **CSP Headers**: Netlify automatic security headers

### Deployment Security
```toml
# Security headers in netlify.toml
[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
```

## Monitoring and Analytics

### Performance Monitoring
- **Web Vitals**: Core Web Vitals tracking
- **Load Times**: Manual performance testing
- **MathJax Performance**: Rendering time monitoring
- **User Experience**: Manual usability testing

### Error Tracking
- **Console Logging**: Browser developer tools
- **MathJax Errors**: Custom error handling
- **Network Errors**: Manual monitoring
- **User Reports**: Direct feedback collection

## Future Technology Considerations

### Potential Upgrades
- **Framework Migration**: Next.js for dynamic features
- **Build System**: Webpack/Vite for optimization
- **CSS Framework**: Tailwind CSS for styling
- **TypeScript**: Type safety for JavaScript
- **Testing Framework**: Jest for unit testing

### Scalability Enhancements
- **CDN Optimization**: Image optimization pipeline
- **Caching Strategy**: Service worker implementation
- **Performance Monitoring**: Real user monitoring
- **Accessibility**: WCAG 2.1 compliance tools

## Constraints and Limitations

### Technical Constraints
- **Static Content**: No dynamic server-side processing
- **No Database**: File-based content management
- **No Authentication**: Client-side password only
- **No Search**: Full-text search not implemented

### Browser Constraints
- **MathJax Dependency**: Requires JavaScript
- **LaTeX Support**: Limited to MathJax capabilities
- **Mobile Performance**: Large mathematical expressions
- **Print Support**: Limited print styling

### Content Constraints
- **Manual Updates**: No automated content pipeline
- **Version Control**: Git-based only
- **Collaboration**: Single-author workflow
- **Localization**: English only

## Best Practices

### Code Quality
- **Semantic HTML**: Proper element usage
- **Accessible Design**: ARIA labels and keyboard navigation
- **Progressive Enhancement**: Graceful degradation
- **Performance First**: Minimal, efficient code

### Content Management
- **Consistent Formatting**: Standardized Markdown
- **Version Control**: Regular commits and clear messages
- **Backup Strategy**: Multiple repository copies
- **Documentation**: Clear content organization

### Deployment
- **Automated Deployment**: Git-based Netlify deployment
- **Environment Parity**: Development matches production
- **Rollback Strategy**: Git-based version control
- **Monitoring**: Regular performance and uptime checks

## How to Keep This File Fresh

- **Quarterly Reviews**: Update based on new dependencies or patterns
- **Performance Monitoring**: Track and optimize based on metrics
- **Security Updates**: Stay current with security best practices
- **Technology Evolution**: Monitor new tools and frameworks
- **User Feedback**: Incorporate performance and usability improvements

