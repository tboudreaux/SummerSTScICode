from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[4.681292,1.023456],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HS_0016+0044/sdB_HS_0016+0044_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HS_0016+0044/sdB_HS_0016+0044_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
