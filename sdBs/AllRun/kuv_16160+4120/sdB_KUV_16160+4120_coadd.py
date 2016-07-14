from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[244.417292,41.214544],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KUV_16160+4120/sdB_KUV_16160+4120_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KUV_16160+4120/sdB_KUV_16160+4120_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
