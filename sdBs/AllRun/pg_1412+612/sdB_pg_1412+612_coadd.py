from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[213.587417,61.018833],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1412+612/sdB_pg_1412+612_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1412+612/sdB_pg_1412+612_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
