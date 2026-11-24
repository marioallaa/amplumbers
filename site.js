'use strict';
const menuButton=document.querySelector('.menu-toggle');
const navigation=document.querySelector('#navigation');
function closeMenu(){navigation?.classList.remove('open');menuButton?.setAttribute('aria-expanded','false')}
menuButton?.addEventListener('click',()=>{const open=menuButton.getAttribute('aria-expanded')!=='true';menuButton.setAttribute('aria-expanded',String(open));navigation.classList.toggle('open',open)});
navigation?.querySelectorAll('a').forEach(link=>link.addEventListener('click',closeMenu));
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&navigation?.classList.contains('open')){closeMenu();menuButton.focus()}});
window.matchMedia('(min-width: 801px)').addEventListener('change',event=>{if(event.matches)closeMenu()});
const filters=document.querySelectorAll('.filter');
const galleryItems=document.querySelectorAll('.gallery-item');
filters.forEach(button=>button.addEventListener('click',()=>{filters.forEach(item=>item.setAttribute('aria-pressed',String(item===button)));let count=0;galleryItems.forEach(item=>{item.hidden=button.dataset.filter!=='all'&&item.dataset.category!==button.dataset.filter;if(!item.hidden)count++});document.querySelector('.gallery-count').textContent=`${count} project photos`}));
const lightbox=document.querySelector('.lightbox');
document.querySelectorAll('.gallery-button').forEach(button=>button.addEventListener('click',()=>{const photo=button.querySelector('img');lightbox.querySelector('img').src=button.dataset.full;lightbox.querySelector('img').alt=photo.alt;lightbox.querySelector('.lightbox-caption').textContent=photo.alt;lightbox.showModal();document.body.style.overflow='hidden'}));
lightbox?.querySelector('.lightbox-close').addEventListener('click',()=>lightbox.close());
lightbox?.addEventListener('click',event=>{if(event.target===lightbox){const rect=lightbox.getBoundingClientRect();if(event.clientX<rect.left||event.clientX>rect.right||event.clientY<rect.top||event.clientY>rect.bottom)lightbox.close()}});
lightbox?.addEventListener('close',()=>{document.body.style.overflow=''});
const enquiryForm=document.querySelector('#enquiry-form');
if(enquiryForm){const requestedService=new URLSearchParams(location.search).get('service');const serviceInput=enquiryForm.elements.service;if([...serviceInput.options].some(option=>option.value===requestedService))serviceInput.value=requestedService;
enquiryForm.addEventListener('submit',event=>{event.preventDefault();if(!enquiryForm.reportValidity())return;const data=new FormData(enquiryForm);const subject=`Website enquiry: ${data.get('service')||'General enquiry'}`;const body=`Name: ${data.get('name')}\nEmail: ${data.get('email')}\nPhone: ${data.get('phone')}\nPostcode: ${data.get('postcode')}\nService: ${data.get('service')}\n\n${data.get('message')}`;const emailUrl=`mailto:info@amplumbing.uk?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;const status=document.querySelector('.form-status');status.replaceChildren(document.createTextNode('Your email draft is ready. Send it in your email app to complete your enquiry. If it did not open, '));const retry=document.createElement('a');retry.href=emailUrl;retry.textContent='open your draft again';status.append(retry,document.createTextNode(' or call +44 7838 628381.'));location.href=emailUrl})}
