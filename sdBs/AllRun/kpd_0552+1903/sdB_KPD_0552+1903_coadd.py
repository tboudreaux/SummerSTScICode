from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[88.918292,19.073956],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KPD_0552+1903/sdB_KPD_0552+1903_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KPD_0552+1903/sdB_KPD_0552+1903_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
