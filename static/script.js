gsap.from(".formm",
    {
        opacity: 0,
        y: 100,
        duration: 1
    });


gsap.from(".formm input",
    {
        scale: 0,
        delay: 1,
        duration: 1
    });



gsap.from(".formm button",
    {
        scale: 0,
        delay: 1,
        duration: 1,
        ease: "bounce.out"
    });


gsap.from(".l label",
    {
        scale: 0,
        delay: 1,
        duration: 1,
        ease: "bounce.out"
    });


gsap.from(".result div",
    {
        y: "-100vh",
        opacity: 0,
        // delay: 1,
        duration: 1,
        ease: "power.out",
        stagger: 0.3
    });

