from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[296.356042,41.092956],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KPD_1943+4058/sdB_KPD_1943+4058_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KPD_1943+4058/sdB_KPD_1943+4058_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
