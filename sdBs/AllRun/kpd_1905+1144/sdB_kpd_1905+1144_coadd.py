from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[287.073583,11.822142],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kpd_1905+1144/sdB_kpd_1905+1144_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kpd_1905+1144/sdB_kpd_1905+1144_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()