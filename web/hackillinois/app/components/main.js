'use client'
import Navbar from './navbar'

export default function Main() {
    return (
    <div className="w-screen h-[3250px] bg-black">
        <Navbar></Navbar>  
        <div className="w-full h-[900px] bg-cover bg-top bg-no-repeat bg-[url('/bot2.jpeg')] opacity-50">
        </div>
        <div className='absolute text-white top-[200px] left-[100px] text-6xl font-bold w-[85%] h-[50px] flex flex-row justify-center items-center opacity-100'>
          Introducing VentureVision - The next step in disaster relief
        </div>
  
      <div className="text-white text-5xl mt-10 font-bold top-20 w-full justify-center flex">
        Use Cases
        </div>
  
      <div className='relative w-auto m-8 pt-12 h-[700px] flex justify-around'>
          <div className="relative rounded-md w-[60%] h-[560px] bg-cover bg-no-repeat bg-[url('/forestfire.jpg')]">
          </div>
          <div className='relative text-white top-40 w-[25%]'>
            <div className="text-5xl mb-8 justify-center text-wrap">
              Forest Fires
            </div>
              <div className="text-3xl justify-center text-wrap">
                VentureVision can be used to detect forest fires and alert the proper authorities
              </div>
          </div>
      </div>
  
      <div className='relative w-[100%] mt-[100px] h-[700px] flex justify-around'>
          <div className='relative top-40 text-white w-[300px]'>
          <div className="text-5xl mb-8 text-wrap">
            Hurricanes
          </div>
          <div className="text-3xl text-wrap">
            VentureVision can be used to detect hurricane damage and alert the proper authorities
          </div>
          </div>          
          <div className="relative rounded-md w-[50%] h-[560px] right-0 bg-cover bg-no-repeat bg-[url('/hurricaneaftermath.jpg')]">
        </div>
      </div>
      
      <div className='relative w-auto m-8 pt-12 h-[500px] flex justify-around'>
          <div className="relative rounded-md w-[60%] h-[560px] bg-cover bg-no-repeat bg-[url('/forestfire.jpg')]">
          </div>
          <div className='relative text-white top-40 w-[25%]'>
            <div className="text-5xl mb-8 justify-center text-wrap">
              Forest Fires
            </div>
              <div className="text-3xl justify-center text-wrap">
                VentureVision can be used to detect forest fires and alert the proper authorities
              </div>
          </div>
      </div>
  
      </div>
    );
  }