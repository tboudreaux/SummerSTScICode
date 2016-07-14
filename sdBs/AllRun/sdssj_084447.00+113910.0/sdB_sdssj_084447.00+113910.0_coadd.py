from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[131.195792,11.65275],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_084447.00+113910.0/sdB_sdssj_084447.00+113910.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_084447.00+113910.0/sdB_sdssj_084447.00+113910.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
