from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[113.356708,36.882667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_073325.61+365257.6/sdB_SDSSJ_073325.61+365257.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_073325.61+365257.6/sdB_SDSSJ_073325.61+365257.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
