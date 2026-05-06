export default function Skeleton(){

    return (
        <div className="animate-pulse bg-gray-50 mt-10 shadow-xl rounded-2xl max-w-4xl w-full grid md:grid-cols-2">
      <div className="eh-64 md:h-auto bg-gray-200 flex justify-center items-center">
      <svg className="w-8 h-8 stroke-gray-400 " viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M20.5499 15.15L19.8781 14.7863C17.4132 13.4517 16.1808 12.7844 14.9244 13.0211C13.6681 13.2578 12.763 14.3279 10.9528 16.4679L7.49988 20.55M3.89988 17.85L5.53708 16.2384C6.57495 15.2167 7.09388 14.7059 7.73433 14.5134C7.98012 14.4396 8.2352 14.4011 8.49185 14.3993C9.16057 14.3944 9.80701 14.7296 11.0999 15.4M11.9999 21C12.3154 21 12.6509 21 12.9999 21C16.7711 21 18.6567 21 19.8283 19.8284C20.9999 18.6569 20.9999 16.7728 20.9999 13.0046C20.9999 12.6828 20.9999 12.3482 20.9999 12C20.9999 11.6845 20.9999 11.3491 20.9999 11.0002C20.9999 7.22883 20.9999 5.34316 19.8283 4.17158C18.6568 3 16.7711 3 12.9998 3H10.9999C7.22865 3 5.34303 3 4.17145 4.17157C2.99988 5.34315 2.99988 7.22877 2.99988 11C2.99988 11.349 2.99988 11.6845 2.99988 12C2.99988 12.3155 2.99988 12.651 2.99988 13C2.99988 16.7712 2.99988 18.6569 4.17145 19.8284C5.34303 21 7.22921 21 11.0016 21C11.3654 21 11.7021 21 11.9999 21ZM7.01353 8.85C7.01353 9.84411 7.81942 10.65 8.81354 10.65C9.80765 10.65 10.6135 9.84411 10.6135 8.85C10.6135 7.85589 9.80765 7.05 8.81354 7.05C7.81942 7.05 7.01353 7.85589 7.01353 8.85Z" stroke="stroke-current" stroke-width="1.6" stroke-linecap="round"></path>
  </svg>
      </div>

      <div className=" p-6 pb-70 flex flex-col justify-between">
        <div>
          <h2 className=" h-3 bg-gray-300 rounded-full  w-48 mb-4">
          </h2>
          <ul className="text-gray-600 mb-2 flex justify-center gap-4">
            <li className="flex items-top gap-2">
              <div className="flex flex-col leading-tight">
                <span className="h-2 bg-gray-300 rounded-full w-16">
                </span>
              </div>
            </li>

            <li className="flex items-top gap-2">
        
              <div className="flex flex-col leading-tight animate-fade animate-delay-550 ">
                <span className="font-semibold "></span>
                <span className="h-2 bg-gray-300 rounded-full w-16"></span>
              </div>
            </li>

            <li className="flex items-top gap-2">
              <div className="flex flex-col leading-tight animate-fade animate-delay-550">
                <span className="font-semibold"></span>
                <span className="h-2 bg-gray-300 rounded-full w-16"></span>
              </div>
            </li>

            <li className="flex items-top gap-2">
            
              <div className="flex flex-col leading-tight animate-fade animate-delay-550">
                <span className="font-semibold"></span>
                <span className="h-2 bg-gray-300 rounded-full w-16"></span>
              </div>
            </li>
          </ul>
          <p className="h-2 bg-gray-300 rounded-full max-w-[380px] mb-2.5 mt-4"></p>
<p className="h-2 bg-gray-300 rounded-full max-w-[340px] mb-2.5"></p>
<p className="h-2 bg-gray-300 rounded-full max-w-[320px] mb-4"></p>
         
          <div className="mb-4">
            <h3 className="h-2.5 bg-gray-300 rounded-full w-34 mb-4"></h3>
            <h4 className="h-1.5 bg-gray-300 rounded-full w-16 mb-1.5"></h4>
            <h4 className="h-1.5 bg-gray-300 rounded-full w-16 mb-1.5"></h4>

          </div>
          <div>
          <h3 className="h-2.5 bg-gray-300 rounded-full w-34 mb-4"></h3>
          <h4 className="h-1.5 bg-gray-300 rounded-full w-16 mb-1.5"></h4>
          <h4 className="h-1.5 bg-gray-300 rounded-full w-16 mb-1.5"></h4>
          </div>
        </div>
      </div>
    </div>

)
}




{/* <div role="status" className="p-4 border border-default rounded-2xl shadow-xl max-w-4xl animate-pulse md:p-6 md:grid-cols-2 ">
    <div role="status" className="flex items-center justify-center h-48 max-w-sm bg-neutral-quaternary rounded-base animate-pulse mb-4 sm:mb-6">
        <svg className="w-11 h-11 text-fg-disabled" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linejoin="round" stroke-width="2" d="m2.25 15.75 5.159-5.159a2.25 2.25 0 0 1 3.182 0l5.159 5.159m-1.5-1.5 1.409-1.409a2.25 2.25 0 0 1 3.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 0 0 1.5-1.5V6a1.5 1.5 0 0 0-1.5-1.5H3.75A1.5 1.5 0 0 0 2.25 6v12a1.5 1.5 0 0 0 1.5 1.5Zm10.5-11.25h.008v.008h-.008V8.25Zm.375 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z"/></svg>
        <span className="sr-only">Loading...</span>
    </div>
    <div className="h-2.5 bg-neutral-quaternary rounded-full w-48 mb-4"></div>
    <div className="h-2 bg-neutral-quaternary rounded-full mb-2.5"></div>
    <div className="h-2 bg-neutral-quaternary rounded-full mb-2.5"></div>
    <div className="h-2 bg-neutral-quaternary rounded-full"></div>
    <div className="flex items-center mt-4">
        <svg className="w-8 h-8 text-fg-disabled me-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18Zm0 0a8.949 8.949 0 0 0 4.951-1.488A3.987 3.987 0 0 0 13 16h-2a3.987 3.987 0 0 0-3.951 3.512A8.948 8.948 0 0 0 12 21Zm3-11a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"/></svg>
        <div>
            <div className="h-2.5 bg-neutral-quaternary rounded-full w-32 mb-2"></div>
            <div className="w-48 h-2 bg-neutral-quaternary rounded-full"></div>
        </div>
    </div>
    <span className="sr-only">Loading...</span>
</div> */}

 


