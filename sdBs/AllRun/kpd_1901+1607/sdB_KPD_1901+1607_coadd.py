from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[285.963833,16.201703],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KPD_1901+1607/sdB_KPD_1901+1607_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KPD_1901+1607/sdB_KPD_1901+1607_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
