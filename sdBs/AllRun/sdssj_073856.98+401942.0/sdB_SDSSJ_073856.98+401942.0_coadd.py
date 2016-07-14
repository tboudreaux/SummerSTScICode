from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[114.737417,40.328333],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_073856.98+401942.0/sdB_SDSSJ_073856.98+401942.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_073856.98+401942.0/sdB_SDSSJ_073856.98+401942.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
