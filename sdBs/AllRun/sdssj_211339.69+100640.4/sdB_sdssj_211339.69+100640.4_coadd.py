from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[318.415375,10.111222],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_211339.69+100640.4/sdB_sdssj_211339.69+100640.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_211339.69+100640.4/sdB_sdssj_211339.69+100640.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()