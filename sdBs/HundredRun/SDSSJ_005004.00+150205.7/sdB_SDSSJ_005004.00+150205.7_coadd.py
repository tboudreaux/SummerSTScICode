from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[187.750005,15.034917],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_005004.00+150205.7/sdB_SDSSJ_005004.00+150205.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_005004.00+150205.7/sdB_SDSSJ_005004.00+150205.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()