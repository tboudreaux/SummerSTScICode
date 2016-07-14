from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[221.738042,58.155583],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_144657.13+580920.1/sdB_sdssj_144657.13+580920.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_144657.13+580920.1/sdB_sdssj_144657.13+580920.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
