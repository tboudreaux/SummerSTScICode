from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[216.689208,-2.532028],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_142645.41-023155.3/sdB_SDSSJ910_142645.41-023155.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_142645.41-023155.3/sdB_SDSSJ910_142645.41-023155.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
