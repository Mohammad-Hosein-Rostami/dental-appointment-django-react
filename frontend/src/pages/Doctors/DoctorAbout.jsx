
const DoctorAbout = ({ doctor }) => {
  return (
    <div>
      <div>
        <h3 className="text-[20px] leading-[30px] text-headingColor font-semibold flex items-center gap-2">
          About
          <span className="text-irisBlueColor font-bold text-[24px] leading-9">
            {doctor?.user?.name}
          </span>
        </h3>
        <p className="text__para">
          {doctor?.about}
        </p>
      </div>

      <div className="mt-12">
        <h3 className="text-[20px] leading-[30px] text-headingColor font-semibold flex items-center gap-2">
          Experience
        </h3>

        <ul className="grid sm:grid-cols-2 gap-[30px] pt-4 md:p-5">
          <li className="p-4 rounded bg-[#fff9ea]">
            <p className="text-[16px] leading-6 font-medium text-textColor">
              {doctor?.major}
            </p>
            <p className="text-[14px] leading-5 font-medium text-textColor">
              {doctor?.experience}
            </p>
          </li>
          
        </ul>
      </div>
    </div>
  );
};

export default DoctorAbout;
