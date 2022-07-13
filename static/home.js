let openMenu = document.querySelector('.hamburger-icon')
let closeMenu = document.querySelector('.menu-close')
let menu = document.querySelector('.menu')
let comp =document.querySelector('.comp')
let links = document.querySelector('.links_quick')
let openMobile = document.querySelector('.profile_mobile')
let profile = document.querySelector('.profile_mob')
let closeMobile = document.querySelector('.closeMobile')
let searchIcon = document.querySelector('.svg-search')
let searchInput = document.querySelector('.nav_mobile_searchBar')
let navInit = document.querySelector('.nav_init')
let closeSearch = document.querySelector('.close_search')

// let ul = document.getElementsByClassName("main_body_jobs");
// let li = ul.querySelectorAll('.main_body_jobs p')
// const listArray = Array.from(li);

openMenu.addEventListener('click', () => {
    menu.style.width = '50vw'
  })
  closeMenu.addEventListener('click', () => {
    menu.style.width = '0%'
  })

  comp.addEventListener('click' , () =>{
    links.classList.toggle('toggle')
  })

  profile.addEventListener('click', () => {
    openMobile.style.width = '100vw'
  })
  closeMobile.addEventListener('click', () => {
    openMobile.style.width = '0%'
  })

  closeSearch.addEventListener('click', () => {
    searchInput.style.display = 'none'
    navInit.style.display = 'flex'
    openMenu.style.display = 'block'
  })

  searchIcon.addEventListener('click', () => {
    searchInput.style.display = 'flex'
    searchInput.style.justifyContent = "space-between"
    navInit.style.display = 'none'
    openMenu.style.display = 'none'
  })
  
  

  // const filterUsers = (event) => {
  //   ul.innerHTML = ""
  //   let keyword = input.value.toLowerCase();
  //   listArray.forEach((item) => {
  //     if (item.textContent.toLowerCase().includes(keyword)) {
  //       ul.appendChild(item)
  //     }
  //   })
  // }
  
  // input.addEventListener('keyup', filterUsers);