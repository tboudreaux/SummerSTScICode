from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[12.779167,0.709192],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0048+004/sdB_pg_0048+004_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0048+004/sdB_pg_0048+004_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
