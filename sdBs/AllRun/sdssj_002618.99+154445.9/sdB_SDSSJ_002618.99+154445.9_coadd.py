from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[6.579125,15.746083],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_002618.99+154445.9/sdB_SDSSJ_002618.99+154445.9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_002618.99+154445.9/sdB_SDSSJ_002618.99+154445.9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
