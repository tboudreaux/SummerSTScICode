from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[249.566542,0.322],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_163815.97-001919.2/sdB_SDSSJ_163815.97-001919.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_163815.97-001919.2/sdB_SDSSJ_163815.97-001919.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
