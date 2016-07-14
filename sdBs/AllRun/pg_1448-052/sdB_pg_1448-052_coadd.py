from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[222.804667,-5.388028],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1448-052/sdB_pg_1448-052_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1448-052/sdB_pg_1448-052_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
