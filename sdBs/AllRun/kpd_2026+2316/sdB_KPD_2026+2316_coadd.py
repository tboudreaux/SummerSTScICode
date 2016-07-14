from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[307.190292,23.460256],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KPD_2026+2316/sdB_KPD_2026+2316_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KPD_2026+2316/sdB_KPD_2026+2316_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
