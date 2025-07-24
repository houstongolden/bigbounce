# Image URLs for BigBounce Project

## Recommended Approach: Use External Image Hosting

Since the PNG files are too large for GitHub (over 3MB total), here are the recommended solutions:

### Option 1: Cloudinary (Free)
1. Sign up at https://cloudinary.com (free tier)
2. Upload your images
3. Get URLs like: `https://res.cloudinary.com/your-account/image/upload/v1/figure1.png`

### Option 2: GitHub Issues Method
1. Create a GitHub issue in your repository
2. Drag and drop images into the issue
3. Copy the generated URLs
4. Use in your HTML

### Option 3: Imgur or Similar
1. Upload to Imgur.com
2. Get direct links
3. Use in your HTML

## Current Image Files:
- figure1_lqg_holst_derivation_enhanced.png (757K)
- figure2_galaxy_spin_comprehensive.png (1.1M)
- figure_3a_tension_resolution.png (510K)
- figure3b_tensions_resolution_comprehensive.png (470K)
- figure6_parameter_naturalness.png (774K)
- figure7_observational_timeline.png (702K)

## Quick Fix: Update HTML to Use External URLs
Once you have external URLs, update the image src attributes in index.html:

```html
<!-- Replace local paths like: -->
<img src="public/images/figure1_lqg_holst_derivation_enhanced.png">

<!-- With external URLs like: -->
<img src="https://res.cloudinary.com/your-account/image/upload/v1/figure1.png">
```

This way your site will work immediately without needing to store large files in Git. 